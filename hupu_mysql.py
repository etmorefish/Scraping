#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-15 13:14:32
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$


import requests
from bs4 import BeautifulSoup
import datetime 
import time 
import MySQLdb

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

import MySQLdb
class MysqlAPI(object):
    def __init__(self, db_ip, db_name, db_password, table_name, db_charset):
        self.db_ip = db_ip
        self.db_name = db_name
        self.db_password = db_password
        self.table_name = table_name
        self.db_charset = db_charset
        self.conn = MySQLdb.connect(host=self.db_ip, user=self.db_name,
                                    password=self.db_password, db=self.table_name, charset=self.db_charset)
        self.cur = self.conn.cursor()
    def add(self,title,post_link,author,author_page,start_data,reply,view,last_reply,date_time):
    	# sql = "CREATE TABLE hupu(id INT NULL AUTO_INCREMENT,\
    	# 						title VARCHAR(100) NOT NULL,\
    	# 						post_link VARCHAR(1000) NOT NULL,\
    	# 						author VARCHAR(20) NOT NULL,\
    	# 						author_page VARCHAR(1000) NOT NULL,\
    	# 						start_data VARCHAR(20) NOT NULL,\
    	# 						reply VARCHAR(20) NOT NULL,\
    	# 						view VARCHAR(20) NOT NULL,\
    	# 						last_reply VARCHAR(20) NOT NULL,\
    	# 						date_time VARCHAR(30) NOT NULL,\
    	# 						PRIMARY KEY(id) )"
        sql = "INSERT INTO hupu(title,post_link,author,author_page,start_data,reply,view,last_reply,date_time)"\
                                   "VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')"

        self.cur.execute(sql %(title,post_link,author,author_page,start_data,reply,view,last_reply,date_time))
        self.conn.commit()


for i in range(1,10):
	link = 'https://bbs.hupu.com/bxj-'+str(i)
	print('开始第%s页数据爬取...' %i)
	soup = get_page(link)
	soup = soup.find('div',class_='show-list')
	post_list = soup.find_all('li')
	data_list = get_data(post_list)
	hupu_post = MysqlAPI('localhost','root','sixqwe123','scraping','utf8')
	for each in data_list:
		hupu_post.add(each[0],each[1],each[2],each[3],each[4],each[5],each[6],each[7],each[8])
	print('第%s页爬取完成！' %i)
	time.sleep(3)

	# CREATE TABLE hupu(id INT NOT NULL AUTO_INCREMENT,title VARCHAR(50) NOT NULL,post_link VARCHAR(1000) NOT NULL, author VARCHAR(20) NOT NULL,author_page VARCHAR(1000) NOT NULL,start_data VARCHAR(20) NOT NULL,reply VARCHAR(20) NOT NULL,view VARCHAR(20) NOT NULL,last_reply VARCHAR(20) NOT NULL,date_time VARCHAR(30) NOT NULL, PRIMARY KEY(id) )	