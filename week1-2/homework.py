from bs4 import BeautifulSoup

with open('/home/ryan/Document/Plan-for-combating-master/week1/1_2/1_2answer_of_homework/index.html','r')as web:
	Soup=BeautifulSoup(web,'lxml')
	images=Soup.select('body > div > div > div > div > div > div > img')
	prices=Soup.select('body > div > div > div > div > div > div > div.caption > h4.pull-right')
	titles=Soup.select('body > div > div > div > div > div > div > div.caption > h4 > a')
	stars=Soup.select('div > div.ratings > p:nth-of-type(2)')
	grades=Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')

for image,price,title,star,grade in zip(images,prices,titles,stars,grades):
	data={
		'title':title.get_text(),
		'price':price.get_text(),
		'image':image.get('src'),
		'star':len(star.find_all("span","glyphicon glyphicon-star")),
		'grade':grade.get_text()
	}
	print(data)
