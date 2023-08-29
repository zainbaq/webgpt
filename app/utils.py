from urllib.parse import urlparse
import os
from dotenv import load_dotenv

def get_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain

def get_openai_key():
    load_dotenv()
    return os.environ['OPENAI_KEY']



