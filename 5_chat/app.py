import flask
import json
import os
from dotenv import load_dotenv
from flask import send_from_directory, request, Flask
from pyngrok import ngrok

load_dotenv()

# Flask app should start in global layout
app = Flask(__name__)
ngrok.set_auth_token(os.getenv('NGROK_AUTH_TOKEN'))
public_url= ngrok.connect(8000).public_url

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    return "Hello World!"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    print(req)

    return {
        'fulfillmentText': 'Hello from the bot world'
    }

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = False
    app.run(port=8000)
