from bs4 import BeautifulSoup
import requests
import time
import pymongo

def getsex(class_name):
	if class_name == ['member_ico']:
		return '男'
	else:
		return '女'

def getlink(url):
	wb_data=requests.get(url)
	soup=BeautifulSoup(wb_data.text,'lxml')
	links = soup.select('#page_list > ul > li > a')
	for link in links:
		href = link.get('href')
		getinfo(href)

def getinfo(url):
	wb_data=requests.get(url)
	soup=BeautifulSoup(wb_data.text,'lxml')
	titles = soup.select('div.pho_info > h4 > em')
	images = soup.select('#curBigImage')
	address = soup.select('div.con_l > div.pho_info > p > span')
	prices = soup.select('div.day_l > span')
	mimgs = soup.select('div.js_box.clearfix > div.member_pic > a > img')
	mnames = soup.select('div.js_box.clearfix > div.w_240 > h6 > a')
	msex = soup.select('div.js_box.clearfix > div.member_pic > div')

	for title,image,price,addres,mimg,mname,sex in zip(titles,images,prices,address,mimgs,mnames,msex):
		data={
			'title':title.get_text(),
			'image':image.get('src'),
			'price':price.get_text(),
			'addres':addres.get_text().strip(),
			'mimg':mimg.get('src'),
			'mname':mname.get_text(),
			'sex':getsex(sex.get('class'))
		}
		houses_tab.insert_one(data)


client = pymongo.MongoClient('localhost',27017)
xiaozhu = client['xiaozhu']
houses_tab = xiaozhu['houses_tab']

# urls=['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,3)]
# for surl in urls:
# 	getlink(surl)

for item in houses_tab.find({'price':{'$gte':'500'}}):
    print(item)