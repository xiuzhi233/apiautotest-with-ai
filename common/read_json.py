"""
-*- coding: utf-8 -*-
 @ Project  : apiautotest
 @ File     : read_json.py
 @ Author   : lifuran
 @ Time     : 2024/12/19 17:27
 @ Describe : 
"""

import json
import os.path

from config.settings import absolute_path


def read_json(filepath):
    """
    根据文件路径读取json文件，并将json文件中的数据转成python文件对象，再返回
    :param filepath:json文件路径
    :return:python文件对象
    """

    # 读之前判断路径合法
    if os.path.isfile(filepath) and filepath.endswith(".json"):
        with open(filepath, mode='r', encoding="utf-8") as f:
            try:
                value = json.load(f)
            except FileExistsError:
                raise FileExistsError("json文件数据编解码错误！")
            else:
                return value
    else:
        raise FileNotFoundError("json文件路径错误！")

if __name__ == '__main__':
    print(read_json(absolute_path('data/sql_data.json')))