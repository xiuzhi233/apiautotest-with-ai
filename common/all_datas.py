"""
-*- coding: utf-8 -*-
 @ Project  : apiautotest
 @ File     : all_datas.py
 @ Author   : lifuran
 @ Time     : 2024/12/22 13:51
 @ Describe : 
"""
from common.MysqlPool import MysqlPool
from common.read_json import read_json
from config.settings import absolute_path


def all_datas(requirement: str, case_id: str = None):
    """

    :param requirement: 需求编号
    :param case_id: 用例编号
    :return:
    """
    datas = MysqlPool().load_table_data("test_case")
    # 传入了case_id表示只取单条case的用例数据
    if case_id:
        for i in datas:
            # 单条用例编号
            if case_id == i[1]:
                if requirement == str(i[0]):
                    i[8] = read_json(absolute_path('data/case_data.json'))[requirement][i[2]][case_id]
                    i[9] = read_json(absolute_path('data/expect_data.json'))[requirement][i[2]][case_id]
                    i[12] = read_json(absolute_path('data/sql_data.json'))[requirement][i[2]][case_id]
                    return i
                else:
                    raise ValueError("需求编号和用例编号不匹配")
            else:
                continue
    # 不传case_id根据需求编号取出所有的用例数据
    else:
        for i in range(len(datas)):
            datas[i][8] = read_json(absolute_path('data/case_data.json'))[requirement][datas[i][2]][datas[i][1]]
            datas[i][9] = read_json(absolute_path('data/expect_data.json'))[requirement][datas[i][2]][datas[i][1]]
            datas[i][12] = read_json(absolute_path('data/sql_data.json'))[requirement][datas[i][2]][datas[i][1]]
            datas[i] = tuple(datas[i])

        return datas


if __name__ == '__main__':
    print(all_datas("4960036655"))
