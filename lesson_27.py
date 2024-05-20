from bs4 import BeautifulSoup
import requests
url = "https://kun.uz"
response = requests.get(url)
if response.status_code == 200:
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    # print(soup)
    arr = soup.find_all('div')
    # print(arr)
    for i in arr:
        # print(i.get('class'))
        if i.get('class') == ['small-news']:
            print(i)      

else:
    print("Failed to retrieve the webpage.")


s = [1,2,3]
s.append(4)

