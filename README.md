# boom
Repo for text and audio-related experiments


### Task 3 Q&A

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