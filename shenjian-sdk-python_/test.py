# -*- coding: utf-8 -*-
import shenjian

user_key = 'a45a69ecec-NjQ0MjJkY2'
user_secret = 'JhNDVhNjllY2VjND-471648259c64422'

########shenjian.Service
service = shenjian.Service(user_key,user_secret)

# 获得应用列表
result = service.get_app_list(page=1, page_size=30)
print(result)
exit()
# 获得爬虫列表
result = service.get_crawler_list(page=1, page_size=30)

# 创建爬虫
result = service.create_crawler(app_name="爬虫名字",code="爬虫代码",app_info='')


########shenjian.Crawler
crawler = shenjian.Crawler(user_key,user_secret,appID)

# 修改爬虫名称信息
result = crawler.edit(app_name="新的名称",app_info="新的info")

 # 使用个人优质版代理IP，代理种类查看shenjian.proxy_type
result = crawler.config_proxy(shenjian.proxy_type.PROXY_TYPE_BETTER)

 # 开启文件云托管
result = crawler.config_host(shenjian.host_type.HOST_TYPE_SHENJIANSHOU)

 # 删除爬虫
result = crawler.delete()

 # 设置爬虫自定义项(不同的爬虫自定义项不同，传递一个dict)
result = crawler.config_custom({"img":True})

#######启动爬虫#########
# 用2个节点启动爬虫
result = crawler.start(2)

#遇到爬取结果停止发现新链接，更新此数据dup_type='change',跳过继续往后爬dup_type='skip',默认为skip
result = crawler.start(dup_type='unspawn')

#覆盖原爬取结果里的数据,默认是保留原数据，插入一条新版本数据change_type='insert'
result = crawler.start(change_type='update')

#定时启动爬虫，该例子为每天爬取一次，更多定时设置与参数详见文档http://docs.shenjian.io/develop/platform/restful/crawler.html#启动爬虫
result = crawler.start(timer_type='daily',time_start='10:00',time_end='23:00')

#######启动爬虫#########

 # 停止爬虫
result = crawler.stop()

# 暂停爬虫
result = crawler.pause()

# 继续爬虫（并设置运行的节点是3个）
result = crawler.resume(3)

# 获取爬虫状态
result = crawler.get_status()

# 获取爬虫速率
result = crawler.get_speed()

# 增加一个运行节点
result = crawler.add_node(1)

# 减少一个运行节点
result = crawler.reduce_node(1)

# 获取爬虫对应的数据源信息
result = crawler.get_source()

# 获取爬虫的Webhook设置
result = crawler.get_webhook()

# 删除爬虫的Webhook设置
result = crawler.delete_webhook()

# 修改爬虫的Webhook设置(设置为新增数据发送webhook，更新数据不发送，自定义数据不发送)
result = crawler.set_webhook(self,"http://www.baidu.com",data_new=True,data_updated=False,msg_custom=False)

 # 获取爬虫的自动发布状态
result = crawler.get_publish_status()

 # 启动自动发布
result = crawler.start_publish(publish_id)

 # 停止自动发布
result = crawler.stop_publish()