"""
-*- coding: utf-8 -*-
 @ Project  : apiautotest
 @ File     : get_sign.py
 @ Author   : lifuran
 @ Time     : 2024/12/19 15:46
 @ Describe : 
"""

import time
import random
import copy
import hashlib
import json


def config_header(data: dict = None, token: str = '', paltform: str = 'java'):
    """
    配置请求头
    @param data:
    @param token:
    @param paltform:
    @return:
    """
    if paltform.lower() == 'java':
        sign = get_java_sign(data)
    elif paltform.lower() == 'php':
        sign = get_php_sign(data)
    else:
        raise ValueError('平台参数错误，请传java或者php')
    return {
        'business': 'YPZP',
        'hybird': 'NO',
        'os': 'WINDOWS',
        'osversion': '10.0',
        'packagename': 'yp.pc',
        'packageversion': '7.6.0',
        'reqsource': 'YPZP',
        'request-source': 'java',
        'runtime': 'PC',
        'runtimeversion': '131.0.0.0',
        'sec-ch-ua': '"Not_A Brand";v="24", "Chromium";v="131", "Google Chrome";v="131"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'token': token,
        'Content-Type': 'application/json',
        'timestamp': sign['timestamp'],
        'nonce': sign['nonce'],
        'sign': sign['sign']
    }


def sorted_params(params, runtime: str = 'pc'):
    """
    定义工具函数，请求参数进行字典排序
    @param params: 参数
    @param runtime: 平台
    @return:
    """
    if runtime.lower() in ['ios', 'android']:
        # runtime为ios/android
        secret_salt = "8k&^$Hsk1?kkcj12^99K1ia"
    else:
        # runtime非ios/android
        secret_salt = "*js1(Uc_m12j%hsn#1o%cn1"
    # 先转成json字符串
    params_json = json.dumps(params, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    # 再把json转成字典对象
    params_dict = json.loads(params_json)
    list_params = list()
    for key in params:
        v = params_dict[key]
        if isinstance(v, (str, int, float)):
            params_dict[key] = str(v)
        if isinstance(v, bool):
            params_dict[key] = str(v).lower()
        elif isinstance(v, (dict, list)):
            params_dict[key] = json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

        list_params.append(f'{key}={params_dict[key]}')
    return ("&".join(list_params)) + '&' + secret_salt


def get_java_sign(data: dict = None, runtime: str = 'pc'):
    """
    生成Java签名信息。

    该函数通过给定的数据生成一个包含时间戳、随机数和签名的字典。
    签名是通过对数据、时间戳和随机数进行SHA-256哈希而生成的。
    @param data:
    @param runtime:
    @return:
    """
    # 生成当前时间的时间戳，单位为毫秒
    timestamp = str(round(time.time() * 1000))
    # 生成一个随机数，范围从1到2^30
    nonce = str(random.randint(1, 2 ** 30))
    # 深拷贝传入的数据，以避免修改原始数据
    data_tmp = copy.deepcopy(data)
    # 如果传入了数据，将时间戳和随机数添加到数据中
    if data:
        data_tmp.update({"nonce": nonce, "timestamp": timestamp})
    else:
        # 如果没有传入数据，创建一个包含时间戳和随机数的字典
        data_tmp = {"nonce": nonce, "timestamp": timestamp}
    # 对数据进行排序并拼接成字符串，以便生成一致的签名
    tmp_str = sorted_params(data_tmp, runtime)
    sign = hashlib.sha256(tmp_str.encode('utf-8')).hexdigest()
    return {"timestamp": timestamp, "nonce": nonce, "sign": sign}


def get_php_sign(data: dict = None):
    """
    生成PHP签名信息。
    该函数根据输入的数据字典生成一个PHP签名信息，包括时间戳、随机数和SHA-256散列值。
    如果提供了数据字典，将会在数据中添加nonce和timestamp字段；如果没有提供，则创建包含这两个字段的新字典。
    最后，根据这些数据生成一个SHA-256散列值，并返回包含时间戳、随机数和散列值的字典。
    @param data:
    @return:
    """
    # 生成当前时间戳（毫秒级）
    timestamp = str(round(time.time() * 1000))
    # 生成随机数nonce，范围从1到2^30之间
    nonce = str(random.randint(1, 2 ** 30))
    # 定义密钥盐值，用于散列计算
    secret_salt = '*js1(Uc_m12j%hsn#1o%cn1'

    # 深拷贝输入数据，以避免修改原始字典
    datatmp = copy.deepcopy(data)
    # 根据是否提供了数据，添加nonce和timestamp字段
    if data:
        datatmp.update({"nonce": nonce, "timestamp": timestamp})
    else:
        datatmp = {"nonce": nonce, "timestamp": timestamp}

    # 初始化临时字典和排序后的数据键列表，用于后续的散列计算
    tmpdict = datatmp
    datasort = sorted(datatmp)

    # 初始化用于生成散列值的字符串
    tmpstr = ''
    # 遍历排序后的键列表，构造散列字符串
    for key in datasort:
        if tmpdict[key]:
            if tmpstr:
                tmpstr += '&'
            tmpstr += str(key) + '=' + str(tmpdict[key])
    # 添加密钥盐值到散列字符串
    tmpstr += '&' + secret_salt

    # 创建SHA-256散列对象
    sign = hashlib.sha256()
    # 更新散列对象的数据，需要将字符串转为字节串
    sign.update(tmpstr.encode())

    # 返回包含时间戳、随机数和散列值的字典
    return {"timestamp": timestamp, "nonce": nonce, "sign": sign.hexdigest()}
