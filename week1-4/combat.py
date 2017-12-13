from bs4 import BeautifulSoup
import requests
import time

url='http://bj.58.com/pbdn/0/?PGTID=0d305a36-0000-1f08-bd6c-1bc03165cc06&ClickID=2'
def geturl(url):
    web_data=requests.get(url)
    soup=BeautifulSoup(web_data.text,'lxml')
    links=soup.select('table > tbody > tr > td.img > a')
    for link in links:
        href=link.get('href')
        if 'zhuanzhuan' in href:
            getinfo(href)


def getinfo(url):
    time.sleep(2)
    web_data=requests.get(url)
    soup=BeautifulSoup(web_data.text,'lxml')
    titles=soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > h1')
    types=soup.select('div > span:nth-of-type(4) > a')
    prices=soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.price_li > span > i')
    addresss=soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.palce_li > span > i')
    hadveiw=soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > p > span.look_time')
    for type,title,price,address,veiw in zip(types,titles,prices,addresss,hadveiw):
        data={
            'type':type.get_text().strip(),
            'title':title.get_text(),
            'price':price.get_text(),
            'address':address.get_text(),
            'veiw':veiw.get_text()
        }
        print(data)

geturl(url)