import requests
from bs4 import BeautifulSoup
import math

headers = {
    'sec-ch-ua': "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
    'sec-ch-ua-mobile': "?0",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "navigate",
    'sec-fetch-user': "?1",
    'sec-fetch-dest': "document",
    'cache-control': "no-cache",
    'postman-token': "97ea517d-9e03-00ec-d6f3-c19a5ea786d5"
}

response = requests.request("GET", 'https://www.gunbuyer.com/', headers=headers)

html = BeautifulSoup(response.content, 'html.parser')

ul = html.find('ul',{'class':'level1 submenu    ui-menu ui-widget ui-widget-content ui-corner-all expanded'})

lis = ul.find_all('li')

for li in lis:
    print (li.text.strip())
    # a_tag = ul.find('a')
    # print (ul.text.strip())
    # cat = 'Knives & Tools/'+ ul.text.strip()
    # file = open('url1.txt', 'a+')
    # file.write(a_tag.get('href') + '===' + cat + '\n')
    # file.close()