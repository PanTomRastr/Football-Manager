from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'http://wildstat.ru/p/7001/ch/all/club1/RUS_Zenit_St_Petersburg/ydate/2017'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("tr",{"class":"tab-row-green"})

#for container in containers:
href = [i.get('href') for i in soup.find_all('a')]