import requests
from bs4 import BeautifulSoup as bs
import time
from proxymanager import ProxyManager

print("### SPLYTOOLS (v1.00) ###")
print("### CODENAME: BLUSH   ###")
print("### BY @hasterestocks ###")
print('\n')

s = requests.session()
proxy_manager = ProxyManager('proxies.txt')
headers = {
    'If-None-Match': 'cacheable:fc82c860b9e5d0f8563edcce5e3827b0',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

delay = input("What delay (in seconds) do you want SPLYTOOLS to be set to? " + "\n")
webhook = raw_input("Please enter the discord webhook you want SPLYTOOLS to send to: " + "\n")

x = 1

while x == 1:
    try:

        proxydict = proxy_manager.next_proxy()
        proxies = proxydict.get_dict()

        response = requests.get('https://yeezysupply.com/products/yeezy-500-blush-soon', headers=headers)
        a = bs(response.text, "html.parser")

        status = a.find("div", {"class":"PI__out-of-stock"}).contents[0]
        preorder = 'PRE ORDER STARTS TOMORROW'



        data = {
            "embeds": [{
                "title": 'SPLY TOOLS',
                "url": 'https://yeezysupply.com/products/yeezy-500-blush-soon',
                "description": "CHANGE FOUND!" + "\n" + "\n" + status,
                "thumbnail": {
                    "url": 'https://cdn.shopify.com/s/files/1/1765/5971/products/01_d940c4e0-db02-4fed-b15b-90b3fee154c4_950x.jpg?v=1518722706'
                    },
                    "color": "16746134",
                    "footer": {
                    "icon_url": "https://pbs.twimg.com/profile_images/929923813420294144/MZX9p4wQ_400x400.jpg",
                    "text": ('Powered by hasterestocks | @hasterestocks')
                    }
                    }]
                    }

        if status == preorder:
            print("No changes!" + " USING PROXY: " + str(proxies))
            time.sleep(delay)
            pass

        else:
            res = s.post(webhook, json=data)
            print("Change found! Posted to discord.")
            time.sleep(10)
    except:
        print("Exception occurred")
        time.sleep(10)
