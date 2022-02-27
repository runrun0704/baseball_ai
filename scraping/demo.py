import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://baseball-data.com/20/"
headers = {
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
}
html = requests.get(url, headers = headers)
soup = BeautifulSoup(html.content, "html.parser")

topic = soup.find('table', attrs = {'class':'standings'})
print(topic.text)