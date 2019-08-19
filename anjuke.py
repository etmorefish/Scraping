#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-11 23:50:53
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$


import requests
from bs4 import BeautifulSoup
from lxml import etree
import time

for i in range(1,3):
	link = 'https://beijing.anjuke.com/sale/p'+str(i)
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	r = requests.get(link,headers = headers)

	soup = BeautifulSoup(r.text,'lxml')
	house_list = soup.find_all('li',class_="list-item")

	for house in house_list:

		name = house.find('div',class_="house-title").a.text.strip()
		price = house.find('span',class_="price-det").text.strip()
		price_area = house.find('span',class_="unit-price").text.strip()
		types = house.find('div',class_="details-item").span.text.strip()
		area = house.find('div',class_="details-item").contents[3].text
		floor = house.find('div',class_="details-item").contents[5].text
		year = house.find('div',class_="details-item").contents[7].text
		# broker = house.find('span',class_="brokername").text
		broker = ''
		address = house.find('span',class_="comm-address").text.strip().replace('\xa0\xa0\n',' ')
		tag_list = house.find_all('span',class_='item-tags')
		tags = [i.text for i in tag_list]
		print(name,price,price_area,types,area,floor,year,broker,address,tags)
		# with open('anjuke.txt',"a+") as f:
		# 	f.write(name)
		# 	f.close()

	time.sleep(5)
		











