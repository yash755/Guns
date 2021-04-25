import requests
from bs4 import BeautifulSoup
import math
import json
import csv


file = open('links2.txt','r')

for f in file:
    data = f
    data = data.replace('\n','')

    data = data.split('===')

    if len(data) >=4:


        url = data[1]
        name = data[0]
        cat = ''
        mfg = ''
        upc = ''
        price = data[2]
        image_0 = data[3]

        desc = ''
        spec = ''

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

        print (url)

        response = requests.request("GET", 'https://www.gunbuyer.com/springfield-9mm-xdm-elite-osp-sprxdme9389cbhcosp-d.html', headers=headers)

        html = BeautifulSoup(response.content, 'html.parser')

        try:

            scripts = html.find_all('script',{'type':'application/ld+json'})

            for script in scripts:
                data = str(script)

                if 'BreadcrumbList' in data:
                    data = data.replace('<script type="application/ld+json">','')
                    data = data.replace('</script>', '')

                    data = json.loads(data)

                    if 'itemListElement' in data:
                        data = data['itemListElement']

                        i = 1
                        for d in data:
                            if i != 1 and i != len(data):
                                if 'item' in d:
                                    subdata = d['item']
                                    if 'name' in subdata:
                                        cat = cat + subdata['name'] + '\\'



                            i = i + 1

                    break

        except:
            print ("script error")

        if cat == '':
            cat = 'Firearms'

        catlen = len(cat)

        if cat[catlen -1 ] == '\\':
            cat = cat[0:catlen -1]

        print (cat)


        try:
            manf = html.find('div',{'class':'manufacturer'})
            sales = manf.find_all('div',{'class':'sale'})

            for sale in sales:
                s_data = sale.text.strip()

                if 'MFG Part Number:' in s_data:
                    mfg = s_data
                    mfg = mfg.replace('MFG Part Number:','')
                    mfg = mfg.strip()

                if 'UPC:' in s_data:
                    upc = s_data
                    upc = upc.replace('UPC:','')
                    upc = upc.strip()


        except:
            print ("Manf Error")


        print (mfg)
        print (upc)


        try:
            desc_data = html.find('div',{'id':'description'})

            desc_data_main = desc_data.text.strip()

            try:
                ul = desc_data.find('ul')
                spec = ul.text.strip()

            except:
                print ("UL error")


            desc_data_main = desc_data_main.replace(spec,'')
            desc = desc_data_main



        except:
            print ("Desc error")


        temp = []
        temp.append(url)
        temp.append(cat)
        temp.append(name)

        if mfg.isdigit():
            temp.append("`" + mfg)
        else:
            temp.append(mfg)
        if upc.isdigit():
            temp.append("`" + upc)
        else:
            temp.append(upc)
        temp.append(price)
        temp.append(desc)
        temp.append(spec)
        temp.append(image_0)


        try:

            scripts = html.find_all('script',{'type':'text/x-magento-init'})

            for script in scripts:
                data = str(script)

                if 'data-gallery-role=gallery-placeholder' in data:
                    data = data.replace('<script type="text/x-magento-init">','')
                    data = data.replace('</script>', '')

                    data = json.loads(data)

                    if '[data-gallery-role=gallery-placeholder]' in data:
                        data = data['[data-gallery-role=gallery-placeholder]']

                        if 'mage/gallery/gallery' in data:
                            data = data['mage/gallery/gallery']

                            if 'data' in data:
                                images = data['data']
                                for image in images:
                                    if 'full' in image:
                                        temp.append(image['full'])

                    break

        except:
            print ("script error")


        print (temp)

        arr = []
        arr.append(temp)

        with open('merge.csv', 'a+') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(arr)


