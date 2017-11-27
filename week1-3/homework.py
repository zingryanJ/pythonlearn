from bs4 import BeautifulSoup
import requests
import time

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
			'标题':title.get_text(),
			'照片':image.get('src'),
			'价格':price.get_text(),
			'地址':addres.get_text().strip(),
			'房主照片':mimg.get('src'),
			'房主名字':mname.get_text(),
			'房主性别':getsex(sex.get('class'))
		}
		print(data)

urls=['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,2)]
for surl in urls:	
	getlink(surl)