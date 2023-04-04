# boom
Repo for text and audio-related experiments

## Task 1: Text
The folder `1_text` contains a Jupyter Notebook on experiments for text classification. It is meant to be run on Google Colab.

## Task 2 Audio

The folder `2_audio` contains a Jupyter Notebook on experiments for text classification. It is meant to be run on Google Colab.

## Task 3 Q&A

The folder `3_QA` contains subdirectory of all related files on experiments for Question and Answer model. 
It is meant to be run on local environment, preferably MacOS.
Following the instructions from [Build a Q&A App with PyTorch](https://towardsdatascience.com/build-a-q-a-app-with-pytorch-cb599480e29)

We first build the Q&A model 

1. Create pipenv
```
pip install virtualenv
virtualenv boom_venv
source boom_venv/bin/activate
```


1. Download Stanford Question Answering Dataset 2.0

```
cd ./3_QA
wget https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json
```

2. Download the Huggingface model using Bash script file `download_model.sh`

```
chmod +x download_model.sh
./download_model.sh
```

3. Install Docker, follow instructions from the official site for:
-  [Mac](https://docs.docker.com/desktop/install/mac-install/) 
- [Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Linux](https://docs.docker.com/desktop/install/linux-install/)

4. After installing Docker. Run the notebook `test_app.ipynb'


## Task 4 Speech

In this experiment, we create a web app for live text-to-speech transcription. 


1. Sign up for Deepgram account and get an API key. Save your API key to a `.env` file, make sure to include the `.env` file in your `.gitignore` file.


2. Create a virtual environment, if you have not done so.
```
python3 -m venv boom_venv
source boom_venv/bin/activate
```

2. Install FastAPI, Deepgram Python SDK

```
pip install "fastapi[all]"
pip install deepgram-sdk
```


4. In case you encounter a error related to WebSocket, to resolve this I did the following:

    - If you are using Mac follow this suggestion in the [StackOverflow thread](https://stackoverflow.com/a/58525755).

    - I followed the suggestion in this [GitHub Issue Comment](https://github.com/websockets/ws/issues/1537#issuecomment-476498391), wherein you have to change the URL to your local machines' WebSocket server. This is line 18 of `4_speech/templates/index.html`. 

5. To run the web app

```
cd 4_speech
uvicorn main:app --reload
```

<!-- 5. For Keyword extraction, I used the RAKE algorithm implementation found in the NLTK package
```
pip install rake-nltk
``` -->

