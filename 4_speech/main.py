from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# from rake_nltk import Rake
from typing import Dict, Callable
from deepgram import Deepgram
from dotenv import load_dotenv
from pyngrok import ngrok
import uvicorn
import os
import re

load_dotenv()

app = FastAPI()
 
dg_client= Deepgram(os.getenv('DEEPGRAM_API_KEY'))
templates = Jinja2Templates(directory="templates")
ngrok.set_auth_token(os.getenv('NGROK_AUTH_TOKEN'))
public_url= ngrok.connect(8000).public_url
# rake_nltk_var= Rake()

# def extract_keywords(text):
#     rake_nltk_var.extract_keywords_from_text(text)
#     keyword_extracted = rake_nltk_var.get_ranked_phrases()
#     return keyword_extracted

def extract_keywords(text):
    keyword_extracted = text.split()
    return keyword_extracted


def vowel_consonant(transcript, keywords):
    con_res= []
    # printing original list
    print("The original keywords are: " + str(keywords))

    vow = "aeiou"
    vow_res = [x for x in keywords if re.search(f"[{vow}]$", x, flags=re.IGNORECASE)]
    con_res = [x for x in keywords if x not in vow_res]
    
    for keyword in con_res:
        transcript= re.sub(keyword, keyword + "-c", transcript) #appends -c for each keyword with consonant

    for keyword in vow_res:
        transcript= re.sub(keyword, keyword + "-v", transcript) #appends -v for each keyword

    return transcript

async def process_audio(fast_socket: WebSocket):
    async def get_transcript(data: Dict) -> None:
        if 'channel' in data:
            transcript = data['channel']['alternatives'][0]['transcript']

            keywords= extract_keywords(transcript)
            transcript= vowel_consonant(transcript, keywords)
            # print("keywords:\t {}" .format(extract_keywords))
            print("resulting transcript:\t {}" .format(transcript))

            if transcript:
                await fast_socket.send_text(transcript)

    deepgram_socket = await connect_to_deepgram(get_transcript)

    return deepgram_socket


async def connect_to_deepgram(transcript_received_handler: Callable[[Dict], None]):
    try:
        socket = await dg_client.transcription.live({'punctuate': True, 'interim_results': False})
        socket.registerHandler(socket.event.CLOSE, lambda c: print(f'Connection closed with code {c}.'))
        socket.registerHandler(socket.event.TRANSCRIPT_RECEIVED, transcript_received_handler)

        return socket
    except Exception as e:
        raise Exception(f'Could not open socket: {e}')


@app.get("/", response_class=HTMLResponse)
def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/listen")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        deepgram_socket = await process_audio(websocket)

        while True:
            data = await websocket.receive_bytes()
            deepgram_socket.send(data)
    except Exception as e:
        raise Exception(f'Could not process audio: {e}')
    finally:
        await websocket.close()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    # uvicorn.run(app, port=8000)