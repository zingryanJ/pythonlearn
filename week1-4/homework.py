from bs4 import BeautifulSoup
import requests

def getherf(url):
	wb_data = requests.get(url)
	soup=BeautifulSoup(wb_data.text,'lxml')
	titles=soup.select('div > ul > li.list-group-item.cards-content > h3 > a')
	#images=soup.select('#mixbox1 > div > ul:nth-of-type(9) > li.list-group-item.img-box > a.mix_img')
	#herf=soup.select('#mixbox1 > div > ul:nth-child(9) > li.list-group-item.img-box > a.mix_img')
	print(soup)


url = 'http://api.yii.dgtle.com/v2/index?token=&perpage=14&page=1'
getherf(url)