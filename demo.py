import requests
from bs4 import BeautifulSoup
import math


file = open('url.txt','r')

for f in file:
    url = f
    url = url.replace('\n','')

    print (url)

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

    response = requests.request("GET", url, headers=headers)

    html = BeautifulSoup(response.content, 'html.parser')


    totalpage = -1

    try:
        number = html.find('span',{'class':'toolbar-number'})
        number = int(number.text.strip())
        print (number)
        totalpage = math.ceil(number/48)

        print (totalpage)

    except:
        print ("error")


    if totalpage != -1:
         page = 1

         while page <= totalpage:


            main_url = url

            main_url = main_url + '?p=' + str(page) + '&product_list_limit=48'

            print (main_url)

            response1 = requests.request("GET", main_url, headers=headers)

            html1 = BeautifulSoup(response1.content, 'html.parser')

            lis = html1.find_all('li',{'class':'item product product-item'})

            for li in lis:
                try:
                    a_tag = li.find('a',{'class':'product-item-link'})

                    name = a_tag.text.strip()
                    link = a_tag.get('href')

                    price = '$0'
                    image = 'none'

                    try:
                        price = li.find('span',{'class':'price'})
                        price = price.text.strip()

                    except:
                        print ("p Errpr")


                    try:
                        image = li.find('img',{'class':'product-image-photo'})
                        image = image.get('src')

                    except:
                        print ("i Errpr")



                    file = open('links2.txt','a+')
                    file.write(name + '===' + link + '===' + price + '===' + image +'\n')
                    file.close()

                except:
                    print ("eor")


            page = page + 1