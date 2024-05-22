import uuid
import json
import requests
from bs4 import BeautifulSoup
url = "https://kun.uz/en"
response = requests.get(url)


if response.status_code == 200:
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    # print(soup)
    arr = soup.find_all('div')
    d = {}
    print(soup)
    for i in arr:
        # print(i.get('class'))
        if i.get('class') == ['container']:
            news_id = str(uuid.uuid4()).split('-')[0]
            # print(i.find_all('img'))            
            # print(type(i.find_all('img')))
            d[news_id] = {"image":list(i.find_all('img'))[0].get('src')}
    print(d)
    with open('news.json', 'a') as file:
        json.dump(d, file)                   

else:
    print("Failed to retrieve the webpage.")



