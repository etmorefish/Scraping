#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-15 11:45:00
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$


import requests
from bs4 import BeautifulSoup
import datetime 
import time 
from pymongo import MongoClient

class MongoAPI(object):
	"""docstring for MongoAPI"""
	def __init__(self, db_ip, db_port,  db_name, table_name):
		# super(MongoAPI, self).__init__()
		self.db_ip = db_ip
		self.db_port = db_port
		self.db_name = db_name
		self.table_name = table_name
		self.conn = MongoClient(host = self.db_ip, port = self.db_port)
		self.db = self.conn[self.db_name]
		self.table = self.db[self.table_name]

	def get_one(self, query):
		return self.table.find_one(query, projection = {"_id": False})
	def get_all(self, query):
		return self.table.find(query)
	def add(self, kv_dict):
		return self.table.insert(kv_dict)
	def delete(self, query):
		return self.table.delete_many(query)
	def check_exist(self,query):
		ret = self.table.find_one(query)
		return ret != None
	# 如果没有会新建
	def update(self, query, kv_dict):
		self.table.update_one(query,{'$set':kv_dict}, upsert = Ture)


# 获取页面内容 此网站使用gzip封装，需要使用r.content进行解封装  由utf-8解码为unicode
def get_page(link):	
	# link = 'https://bbs.hupu.com/bxj'
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	r = requests.get(link,headers = headers)
	html = r.content
	html = html.decode('UTF-8')
	soup = BeautifulSoup(html,"lxml")
	return soup

#对返回的HTML信息进行处理的到虎扑步行街list信息
def get_data(post_list):
	data_list = []
	for post in post_list:
		title = post.find('div',class_="titlelink box").a.text.strip()
		post_link =  post.find('div',class_="titlelink box").a['href']
		post_link = 'https://bbs.hupu.com'+post_link
		author_div = post.find('div',class_="author box")
		author = author_div.find('a',class_="aulink").text.strip()
		author_page = author_div.find('a',class_="aulink")['href']
		start_date = author_div.select('a:nth-of-type(2)')[0].get_text()
		reply_view = post.find('span',class_='ansour box').text.strip()
		reply = reply_view.split('/')[0].strip()
		view = reply_view.split('/')[1].strip()
		reply_div = post.find('div',class_="endreply box")
		reply_time = reply_div.a.text.strip()
		last_reply = reply_div.find('span',class_='endauthor').text.strip()
		date_time = str(datetime.date.today())+' '+ reply_time
		data_list.append([title,author,post_link,author_page,start_date,reply,view,last_reply,date_time])
	return data_list
for i in range(1,10):
	link = 'https://bbs.hupu.com/bxj-'+str(i)
	print('开始第%s页数据爬取...' %i)
	soup = get_page(link)
	soup = soup.find('div',class_='show-list')
	post_list = soup.find_all('li')
	data_list = get_data(post_list)

	hupu_post = MongoAPI('localhost', 27017, 'hupu', 'post')
	for each in data_list:
		hupu_post.add({"title" : each[0],
						"author" : each[1],
						"post_link" : each[2],
						"author_page" : each[3],
						"start_date" : str(each[4]),
						"reply" : each[5],
						"view" : each[6],
						"last_reply" : each[7],
						"last_reply_time" : str(each[8])


			})
	print('第%s页爬取完成！' %i)
	time.sleep(3)





