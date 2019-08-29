#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'github.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
s = requests.session()
s.headers.update(headers)


def get_token():
    url = 'https://github.com/login'
    response = s.get(url, timeout=10)
    pat = 'name=\"authenticity_token\" value=\"(.*?)\"'
    return re.findall(pat, response.text)[0]


def login(authenticity_token, account, password):
    payload = {
        'commit': 'Sign in',
        'utf8': '\u2713',
        'authenticity_token': authenticity_token,
        'login': account,
        'password': password,
    }
    url = 'https://github.com/session'
    response = s.post(url, data=payload)
    print(response.text)
    # do whatever you want


if __name__ == '__main__':
    account, password = '', ''
    authenticity_token = get_token()
    login(authenticity_token, account, password)


