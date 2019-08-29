# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import requests, time, hashlib, base64


class _Base(object):
    def __init__(self, user_key, user_secret):
        timestamp = str(int(time.time()))
        sign = str(user_key) + timestamp + str(user_secret)
        md5 = hashlib.md5()
        md5.update(sign.encode('utf-8'))
        sign = md5.hexdigest()
        self.params = {'user_key': user_key, 'timestamp': timestamp, 'sign': sign}

    def _request(self, url='', params=None, method='get', data=None, timeout=60):
        try:
            url = "http://www.shenjian.io/rest/v3/" + url
            params_get = dict(self.params)
            if isinstance(params, dict):
                params_get.update(params)
            if method == 'get':
                result = requests.get(url, params=params_get, timeout=timeout)
            else:
                result = requests.post(url, params=params_get, data=data, timeout=timeout)
            return result.json()
        except BaseException:
            raise IOError("request error")


class Service(_Base):
    def get_money_info(self):
        return self._request("user/money")

    def get_node_info(self):
        return self._request("user/node")

    def get_app_list(self, page=1, page_size=50, deleted=False):
        return self._request("app/list", method='post', data={'page': page, 'page_size': page_size, 'deleted': deleted})

    def get_crawler_list(self, page=1, page_size=50, deleted=False):
        return self._request("crawler/list", method='post',
                             data={'page': page, 'page_size': page_size, 'deleted': deleted})

    def create_crawler(self, app_name, app_info='', code=''):
        data = {'app_name': app_name, 'app_info': app_info}
        if code != '':
            data['code'] = base64.b64encode(code.encode("utf-8"))
        return self._request("crawler/create", method='post', data=data)


class Crawler(_Base):
    def __init__(self, user_key, user_secret, app_id):
        _Base.__init__(self, user_key, user_secret)
        app_id = str(app_id)
        if not app_id.isdigit():
            raise TypeError('app_id is not a digit')
        self.url = "crawler/" + str(app_id)

    def edit(self, app_name, app_info=''):
        return self._request(self.url + "/edit", method='post', data={'app_name': app_name, 'app_info': app_info})

    def config_proxy(self, proxy):
        try:
            proxy = int(proxy)
            return self._request(self.url + "/config/proxy", method='post', data={'proxy': proxy})
        except ValueError:
            raise ValueError('there is no this type proxy')

    def config_host(self, host, image=True, text=False, audio=False, video=False, application=False):
        try:
            host = int(host)
            data = {'host': host}
            if image:
                data['image'] = True
            if text:
                data['text'] = True
            if audio:
                data['audio'] = True
            if video:
                data['video'] = True
            if application:
                data['application'] = True
            return self._request(self.url + "/config/host", method='post', data=data)
        except ValueError:
            raise ValueError('there is no this type host')

    def config_log(self, less_log):
        return self._request(self.url + "/config/log", method='post', data={less_log: less_log})

    def config_custom(self, custom_param):
        for key in custom_param:
            if isinstance(custom_param[key], list) and not key.endswith('[]'):
                custom_param[key+'[]'] = custom_param[key]
                custom_param.pop(key)
        return self._request(self.url + "/config/custom", method='post', data=custom_param)

    def start(self, node=1, follow_new=True, follow_change=False, dup_type='skip', change_type='insert', **timer):
        data = {'node': node}
        if follow_new:
            data['follow_new'] = follow_new
        if follow_change:
            data['follow_change'] = follow_change
        data['dup_type'] = dup_type
        data['change_type'] = change_type
        data.update(timer)
        return self._request(self.url + "/start", method='post', data=data)

    def stop(self):
        return self._request(self.url + "/stop")

    def pause(self):
        return self._request(self.url + "/pause")

    def resume(self, node=1):
        return self._request(self.url + "/resume", method='post', data={'node': node})

    def get_status(self):
        return self._request(self.url + "/status")

    def get_speed(self):
        return self._request(self.url + "/speed")

    def add_node(self, node=1):
        try:
            node = int(node)
        except ValueError:
            raise ValueError('please input right node num')
        return self._request(self.url + "/node", method='post', data={'node_delta': node})

    def reduce_node(self, node=1):
        try:
            node = -int(node)
        except ValueError:
            raise ValueError('please input right node num')
        return self._request(self.url + "/node", method='post', data={'node_delta': node})

    def get_source(self):
        return self._request(self.url + "/source")

    def get_webhook(self):
        return self._request(self.url + "/webhook/get")

    def set_webhook(self, webhook_url, data_new=True, data_updated=False, msg_custom=False):
        data = {"webhook": webhook_url}
        if data_new:
            data['data_new'] = data_new
        if data_updated:
            data['data_updated'] = data_updated
        if msg_custom:
            data['msg_custom'] = msg_custom
        return self._request(self.url + "/webhook/set", method='post', data=data)

    def delete_webhook(self):
        return self._request(self.url + "/webhook/delete")

    def start_publish(self, publish_id):
        try:
            if isinstance(publish_id, (int, str)):
                publish_id = [int(publish_id)]
            elif isinstance(publish_id, (list, tuple)):
                publish_id = [int(x) for x in publish_id]
        except ValueError:
            raise ValueError('publish_id is illegal')
        return self._request(self.url + "/autopublish/start", method='post', data={'publish_id[]': publish_id})

    def stop_publish(self):
        return self._request(self.url + "/autopublish/stop")

    def get_publish_status(self):
        return self._request(self.url + "/autopublish/status")

    def delete(self):
        return self._request(self.url + "/delete")
