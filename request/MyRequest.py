"""
-*- coding: utf-8 -*-
 @ Project  : apiautotest
 @ File     : MyRequest.py
 @ Author   : lifuran
 @ Time     : 2024/12/19 15:45
 @ Describe : 封装接口请求
"""

import json
import requests
import urllib3

from common.ReadConfig import ReadConfig

from config.settings import *
from request.get_sign import config_header

read_ini = ReadConfig()


class MyRequest:
    # 忽略“正在发出未验证的HTTPS请求，强烈建议添加证书验证”警告
    urllib3.disable_warnings()

    def __init__(self, env):
        self.session = requests.sessions.Session()
        self.goss_host = read_ini.get_host(f'goss-{env}')
        self.yupao_host = read_ini.get_host(f'yupao-{env}')

    # 封装请求方法
    def my_request(self, method, api, mime, data, headers: dict = Header):
        """
        封装请求
        :param method: 请求方法
        :param api: 接口路径
        :param mime: 媒体类型
        :param data: 请求数据
        :param headers: 请求头
        :return: Response Type
        """
        self.session.headers.update(headers)
        url = self.goss_host + api

        # 判断媒体类型是否为表单类型，如果是，使用data传参
        if mime == "application/x-www-form-urlencoded" or mime == "x-www-form-urlencoded":
            return self.session.request(method=method, url=url, data=data)

        # 判断媒体类型是否为json传参，如果是，使用json传参
        elif mime == "application/json" or mime == "json":
            return self.session.request(method=method, url=url, json=data)

        # 判断媒体类型是否为上传文件，如果是，使用files传参
        elif mime == "multipart/form-data" or mime == "form-data":
            return self.session.request(method=method, url=url, files=data)

        # 判断媒体类型是否为地址栏传参，如果是，使用params传参
        elif mime == "query" or mime == "param":
            return self.session.request(method=method, url=url, params=data)

        # 判断媒体类型是否为None，表示没有传参
        elif mime is None:
            return self.session.request(method=method, url=url, data=None, json=None, params=None, files=None)

        # 判断媒体类型是否query|json，表示地址栏和请求体中同时传参，使用params和json同时传参
        elif mime == "query|json" or mime == "json|query" or mime == "params|json":
            return self.session.request(method=method, url=url, params=data["query"], json=data["json"])

        # 判断媒体类型是否text或者为text/plain，表示请求体中纯文本，使用data传参
        elif mime == "text" or mime == "text/plain":
            return self.session.request(method=method, url=url, data=data)

        else:
            raise NameError("传入的媒体类型，没有封装，请自行封装!")

    def __del__(self):
        self.session.close()


if __name__ == '__main__':
    MyRequest('test').my_request("POST", "", "json", {"name": "test"})
