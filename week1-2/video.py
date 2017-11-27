from bs4 import BeautifulSoup
info = []
with open('/home/ryan/Document/Plan-for-combating-master/week1/1_2/1_2code_of_video/web/new_index.html','r') as wb_data:
	Soup = BeautifulSoup(wb_data,'lxml')
	images = Soup.select('body > div.main-content > ul > li > img')
	titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
	descs = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
	rates = Soup.select('body > div.main-content > ul > li > div.rate > span')
	cates = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')


#	print(images,titles,descs,rates,cates,sep='\n-----------\n')

for title,image,desc,rate,cate in zip(titles,images,descs,rates,cates):
	data={
		'title':title.get_text(),
		'rate':rate.get_text(),
		'desc':desc.get_text(),
		'cate':list(cate.stripped_strings),
		'image':image.get('src')
	}
	info.append(data)

for i in info:
	if float(i['rate'])>3:
		print(i['title'],i['cate'])



'''
body > div.main-content > ul > li:nth-child(1) > img
body > div.main-content > ul > li:nth-child(1) > div.article-info > h3 > a
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.meta-info > span:nth-child(2)
body > div.main-content > ul > li:nth-child(1) > div.rate > span
body > div.main-content > ul > li:nth-child(1) > div.article-info > p.description
'''