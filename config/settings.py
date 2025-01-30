"""
-*- coding: utf-8 -*-
 @ Project  : apiautotest
 @ File     : settings.py
 @ Author   : lifuran
 @ Time     : 2024/12/19 16:26
 @ Describe : 
"""
import os

Cookie = 'areaInfo=%7B%22id%22%3A1%2C%22pid%22%3A%22%22%2C%22name%22%3A%22%E5%85%A8%E5%9B%BD%22%2C%22nameA%22%3A%22%EF%BB%BF%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%22%2C%22ltr%22%3A%22quanguo%22%2C%22lv%22%3A1%2C%22adcode%22%3A%22100000%22%7D; Hm_lvt_14752563c89f0870e93d2f6ac497f815=1736126946; HMACCOUNT=19F502F09E8D1654; cookieHostname=mms-test.yupaowang.com; jwtToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0ZW5hbnRzIjpbImFtcyIsImFtcyIsImNtcyIsIm1tcyIsInJjcyIsInl1cGFvIl0sIm9wZW5JZCI6Im91XzBlMTcwYzM1MjdkMTg1ZDNiYjI5NGQyMGIwZmRiMDlhIiwidXNlck5hbWUiOiLmnY7npo_lhokiLCJleHAiOjE3MzY3MzIyNTMsInVzZXJJZCI6IjE5NWVjZWMyIn0.Vsxncn34so6yCdIRWiHjmWx4lYwzQPgDlMHlA3WyL4k; Hm_lpvt_14752563c89f0870e93d2f6ac497f815=1736129462; TOKEN=%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MzYxMjk0NzcsImV4cCI6MTc0NjQ5NzQ3NywiZGF0YSI6eyJzaW5nbGUiOiJIOTRHVVVBRFM2UVZFOFZIIiwidWlkIjoxNjI4OTc3NjcsImJ1c2luZXNzIjoiMSIsInN5c3RlbV90eXBlIjoiY29tcHV0ZXIiLCJtaW5pX3Rva2VuIjoiSDk0R1VVQURTNlFWRThWSCIsImlkIjoxNjI4OTc3NjcsInV1aWQiOjE2Mjg5Nzc2N30sInRva2VuIjp7InJlZ1J0IjoicGMiLCJ0ZW5hbnRLZXkiOiJZUFpQIiwidGVuYW50SWQiOjE2Mjg5Nzc2NywicGFja2FnZU5hbWUiOiJ5cC5wYyIsInVzZXJJZCI6MTYyODk3NzY3LCJ0b2tlbiI6Ikg5NEdVVUFEUzZRVkU4VkgifX0.UNAq0fv3I-GmsSdpEKLHZnpDYDB34As9QzynrvfmGuM%22; USERID=162897767'
Header = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'Connection': 'keep-alive',
    'Content-Length': '50',
    'Content-Type': 'application/json',
    'Cookie': Cookie,
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows'
}


def absolute_path(file_name):
    """
    获取当前项目的根目录，并将传入的文件路径拼接成绝对路径
    :param file_name:
    :return: 绝对路径
    """
    current_path = os.path.abspath(__file__)
    current_path_dir = os.path.dirname(current_path)
    current_path_dir_parent = os.path.dirname(current_path_dir)
    # 兼容Windows、Linux、Macos系统路径格式
    file_name = file_name.replace('/', os.sep)
    file_name = file_name.lstrip(os.sep)
    file_name = file_name.replace('\\', os.sep)
    return os.path.join(current_path_dir_parent, file_name)
