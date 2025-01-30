"""
-*- coding: utf-8 -*-
 @ Project  : apiautotest
 @ File     : ReadConfig.py
 @ Author   : lifuran
 @ Time     : 2024/12/19 15:55
 @ Describe : 
"""
import configparser
import os

from config.settings import absolute_path


class ReadConfig(object):
    def __init__(self):
        # 目录
        self.project_path = os.path.dirname(os.path.dirname(__file__))
        # config dir
        self.config_dir_path = os.path.join(self.project_path, 'config')
        # config.ini file
        config_ini_path = os.path.join(self.config_dir_path, "config.ini")
        self.dataconfig_path = os.path.join(self.project_path, "data")
        self.conf = configparser.ConfigParser()
        self.conf.read(config_ini_path, encoding="utf-8")

    def get_host(self, key):
        """
        根据key获取host域名
        :param key: [HOST]
        :return: host地址
        """
        try:
            _host = self.conf.get("HOST", key)
        except KeyError:
            raise KeyError("ini配置文件下HOST节点传入的key错误！")
        else:
            return _host

    def get_mysql_connection(self, key):
        """
        根据key获取数据库的连接信息
        :param key:
        :return:
        """
        try:
            _message = self.conf.get('MYSQL', key)
        except KeyError:
            raise KeyError("ini文件下MYSQL节点传入的key错误！")
        else:
            return _message

    def get_case_file(self, key):
        """
        根据key获取用例文件的路径
        :param key:
        :return:
        """
        try:
            _path = absolute_path(self.conf.get('CASE_FILE', key))
        except KeyError:
            raise KeyError("ini文件下CASE_FILE节点传入的key错误！")
        else:
            return _path

    def get_run_env(self, key):
        """
        根据key获取运行环境
        :param key:
        :return:
        """
        try:
            _env = self.conf.get('RUN_ENV', key)
        except KeyError:
            raise KeyError("ini文件下RUN_ENV节点传入的key错误！")
        else:
            return _env


if __name__ == '__main__':
    print(ReadConfig().get_run_env('ENV'))
