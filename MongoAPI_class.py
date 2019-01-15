#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-15 11:16:56
# @Author  : lilei (849078367@qq.com)
# @Link    : http://www.xxml.xyz
# @Version : $Id$


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




