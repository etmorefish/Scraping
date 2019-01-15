#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-15 16:45:52
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$


import requests
from bs4 import BeautifulSoup
import time 

with open('alexa.txt','w') as f:
	for i in range(100):
		link = 'http://www.alexa.cn/siterank/'+str(i)
		headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
		r = requests.get(link,headers = headers)
		html = r.content
		html = html.decode('UTF-8')

		soup = BeautifulSoup(html,'lxml')

		soup = soup.find('ul',class_="siterank-sitelist")
		link_list = soup.find_all('li')

		# for link in link_list:
			# urls = link.find('div',class_="domain").a.text.strip()

		for link in link_list:
			urls = link.find('div',class_="domain").a.text.strip()
			f.write(urls)
			f.write("\n")
		print('第%s页爬取完成！' %(i+1))
		time.sleep(2)
		