
import requests # regular expressions
import argparse

from bs4 import BeautifulSoup
from urllib.parse import urljoin

parser = argparse.ArgumentParser(description="SEO CLI Tool")
parser.add_argument("url", type=str, help="The URL of the webpage to analyze")
args = parser.parse_args()
url = args.url

header = {
    
}