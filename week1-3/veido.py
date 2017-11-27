from bs4 import BeautifulSoup
import requests

url = "https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html"
wb_data=requests.get(url)
soup=BeautifulSoup(wb_data.text,'lxml')
titles =soup.select('div.listing_title > a[target="_blank"]')
images = soup.select('img[width="180"]')
cates = soup.select('div.p13n_reasoning_v2')
print(titles)
'''
for title,image,cate in zip(titles,images,cates):
	data={
		'title':title.get_text(),
		'img':image.get('src'),
		'cate':list(cate.stripped_strings)
	}
	print(data)

headers = {
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
	'Cookie':'ServerPool=A; TAUnique=%1%enc%3Ac%2B8%2B2SlSSKqt6KnMsBnlnCKeD4aD39dUyZWVfWJMSd6RqDIW%2BjDBvQ%3D%3D; TASSK=enc%3AAO938knDfshIsxOfCuRLBUQhEUxkjLx4%2BxDzUD3gnlQh6F6XXzUpvv5IexwB2srHRG9lDW03wRO%2FgD8y0uUevbbIfU4DZ6kF4fdHpvqZMs6M%2F6DnCgnWfqR5qLXWvsuqIg%3D%3D; TAPD=tripadvisor.cn; _smt_uid=5a1689b7.1ed995b9; __gads=ID=fce5b49c97b8dab8:T=1511426487:S=ALNI_MZ3IWLz3BE4DppNQb2cgOVrl33Fbg; SecureLogin2=3.4%3AAGLOelW%2BRFQsy7yH6yMKxjkqXBvPcyNLHYD40%2FGBTItZ2EwqbjA6feHwhRT9NYwFBrN8feneBOQ9iplXoru0qQMrB6BuWA65bMQ%2Bll7%2B04H8HbBpojiuu3tWMZx1uwz9UDvwSQPoa5psZIVOfgOdYMrmHpOky7ZMr2bRKeyNDFws5vJRW%2FtAOmpv86ei5187h5WTx51dzcJm3CIw6zeXvKU%3D; TAAuth3=3%3A2a922b49cce315821449d4983d3cc02d%3AADXffBucIJdbw96rXmvk8Zf072MmgExQZZ5FVbh0GiN67YOAz7VoHzv%2FlSEYxMESuGoCdCLiMGBYqTxwcTDL%2FCMxCT14w8Zb3lTDVYgzxlLCKH6lw%2B0dJHvuBuBsdEoX0C5VnqQXaWI4msz61hadbBdNNsTQGPuHCP3w41cnsg04pjWOZH1YVtjOvx9TQeudTg%3D%3D; CommercePopunder=SuppressAll*1511429903090; BEPIN=%1%15fe83e503a%3Bbak11c.daodao.com%3A10023%3B; _gat_UA-79743238-4=1; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C1%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FSmartDeals-g60763-d1687489-The_National_9_11_Memorial_Museum-New_York_City_New_York-Hotel-Deals.html; roybatty=TNI1625!AGUoB53ZpkDz7tDU68G6gWXqSB8UdgbV9iIJTuYzm4XVCUSHiHkfFyRW6QSIJTTDMuhE9AobjfpZ%2BIpv6oIS4hbRPpXg0VdPGMQ%2FSKF%2B8Cij0EOs3pOwfuryEHKZXAbGmE35iwX3fJbd0hOqN%2F95u0ZAvFeCE%2F8dkJIiwUIi0C6g%2C1; _ga=GA1.2.852328925.1511426486; _gid=GA1.2.1276677754.1511426486; ki_t=1511426493837%3B1511426493837%3B1511429988688%3B1%3B12; ki_r=; TASession=%1%V2ID.D390BEF7FCFDC73C460E2E9862204D00*SQ.65*LP.%2FLangRedirect%3Fauto%3D3%26origin%3Dzh%26pool%3DA%26returnTo%3D%252F*PR.427%7C*LS.DemandLoadAjax*GR.53*TCPAR.22*TBR.1*EXEX.70*ABTR.91*PHTB.86*FS.98*CPU.59*HS.featured*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.DB906014DEABF1CB46575C5F84641C9B*LF.zhCN*FA.1*DF.0*IR.3*OD.zh*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.1687489; TATravelInfo=V2*AY.2017*AM.12*AD.3*DY.2017*DM.12*DD.4*A.2*MG.-1*HP.2*FL.3*RVL.60763_327l105127_327l1687489_327*DSM.1511429989182*RS.1; TAUD=LA-1511426485099-1*RDD-1-2017_11_23*HDD-3433421-2017_12_03.2017_12_04*LD-3504061-2017.12.3.2017.12.4*LG-3504063-2.1.F.'
}

url_saves='https://www.tripadvisor.cn/Saves/927031'
wb_data = requests.get(url_saves,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')

titles=soup.select('div > div.saves-location-details.ui_media > div.media-content > div > a')
print(titles)
'''
