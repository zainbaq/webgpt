# WebGPT

WebGPT is a simple command line assistant that can converse and give you information found on an (non-Javascript) website! It is still in development, so there's no conversational memory, but you can ask it questions about content found at the domain provided.

## Quickstart
Create a virtual environment and install packages from requirements.txt
```
python -m venv <your-virtual-env>
source ./bin/activate
pip install -r requirements.txt
```

Run the app in 'Research' mode with the -r flag. This will tell the app to research the url provided and extract all textual information.
```
python ./app/run.py -u <url> -r
```

If you have already done the step above once and the data/processed directory has 2 files. You can omit the -r flag to skip the research.
```
python ./app/run.py -u <url>
```

