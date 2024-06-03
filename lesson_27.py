import uuid
import json
import requests
from bs4 import BeautifulSoup
url = "https://kun.uz/en"
response = requests.get(url)


inf response.status_code == 200:
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    # print(soup)
    arr = soup.find_all('div')
    d = {}
    print(soup)
    for i in arr:
        # print(i.get('class'))
        if i.get('class') == ['small-news']:
            news_id = str(uuid.uuid4()).split('-')[0]
            # print(i.find_all('img'))            
            # print(type(i.find_all('img')))
            s = i.find_all('span')
            text_inside_span = [span.get_text() for span in s]
            print(text_inside_span[0])
        
            # d.find_all('div')
            # print(s)
            # if s[0].get('class') == ['small-news__content']:
            #     s.get
            d[news_id] = {"image":list(i.find_all('img'))[0].get('src'),"created_at":text_inside_span[0]}
    print(d)
    with open('news.json', 'w') as file:
        json.dump(d, file)                   

else:
    print("Failed to retrieve the webpage.")


