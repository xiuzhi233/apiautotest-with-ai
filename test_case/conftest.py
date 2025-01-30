"""
-*- coding: utf-8 -*-
 @ Project  : apiautotest
 @ File     : conftest.py
 @ Author   : lifuran
 @ Time     : 2024/12/22 15:14
 @ Describe : 
"""
import pytest

from common.ReadConfig import ReadConfig
from request.MyRequest import MyRequest


# 请求方法装饰器
@pytest.fixture(scope='session')
def req_fixture():
    yield MyRequest(ReadConfig().get_run_env('ENV'))
