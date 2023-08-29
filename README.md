# WebGPT

WebGPT is a simple command line assistant that can converse and give you information found on an (non-Javascript) website! It is still in development, so there's no conversational memory, but you can ask it questions about content found at the domain provided.

*REQUIRES PYTHON*

## Quickstart
Clone the repository
```
git clone https://github.com/zainbaq/webgpt.git
cd webgpt
```
Create a virtual environment and install packages from requirements.txt
```
python -m venv <your-virtual-env>
source ./bin/activate
pip install -r requirements.txt
```
Create a file called '.env' in the folder and add your OpenAI API key. Make sure you don't post your code with your API Key anywhere.
```
touch ./.env

# add this line to the file
OPENAI_KEY=<your-openai-api-key-here>
```

Run the app in 'Research' mode with the -r flag. This will tell the app to research the url provided and extract all textual information.
```
python ./app/run.py -u <url> -r
```

If you have already done the step above once and the data/processed directory has 2 files, you can omit the -r flag to skip the research phase.
```
python ./app/run.py -u <url>
```

