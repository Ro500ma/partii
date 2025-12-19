import requests
from bs4 import BeautifulSoup

parties = []

url = "https://minjust.gov.ru/ru/pages/politicheskie-partii/"
headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/127.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            }
try:
        response = requests.get(url, headers=headers, timeout=10)
        
        
except requests.exceptions.RequestException as e:
        print(e)

soup = BeautifulSoup(response.text, 'html.parser')
list = soup.find('ol')
list_items = list.find_all('li')
for item in list_items:
        link_tag = item.find('a')
        tag_url = link_tag.get('href')
        if tag_url:
            if tag_url.startswith('http'):
                item_url = tag_url
            else:
                item_url = "https://minjust.gov.ru" + tag_url
        else:
             item_url = None
        party_name = link_tag.get_text().strip().replace('\xa0', ' ')
        parties.append({
            "name": party_name,
            "doc_url": item_url
        })
print(parties)

