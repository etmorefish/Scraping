import requests
from lxml import etree

url = 'https://www.hao123.com'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(url,headers = headers)
res = etree.HTML(r.text)

links = {}

banner = res.xpath('//div[@monkey="mingzhan-zfsitebar"]/a/text()')
banner_link = res.xpath('//div[@monkey="mingzhan-zfsitebar"]/a/@href')
banners = dict(zip(banner,banner_link))
links.update(banners)


site_name =res.xpath('//div[@monkey="site"]//li//a/text()')
site_link =res.xpath('//div[@monkey="site"]//li//a/@href')
sites = dict(zip(site_name,site_link))
links.update(sites)

block_name = res.xpath('//div[@monkey="coolsites"]/div/ul/li[1]/a/text()')
block_link = res.xpath('//div[@monkey="coolsites"]/div/ul/li[1]/a/@href')
for i in range(len(block_name)):
    block_row_name = res.xpath('//div[@monkey="coolsites"]/div/ul[{}]/li//a/text()'.format(i+1))
    block_row_link = res.xpath('//div[@monkey="coolsites"]/div/ul[{}]/li//a/@href'.format(i+1))
    block = dict(zip(block_row_name,block_row_link))
    links.update(block)

print(links,len(links))
