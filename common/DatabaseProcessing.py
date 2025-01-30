"""
-*- coding: utf-8 -*-
 @ Project  : apiautotest
 @ File     : DatabaseProcessing.py
 @ Author   : lifuran
 @ Time     : 2024/12/19 17:41
 @ Describe : 获取所有的用例，转成二维列表
"""
from common.MysqlPool import MysqlPool
from common.ReadConfig import ReadConfig
from common.read_json import read_json


class DatabaseProcessing:

    def __init__(self):
        """
        加载用例数据
        """
        read_config = ReadConfig()
        case_data_path = read_config.get_case_file('CASE_DATA_JSON')
        expect_data_path = read_config.get_case_file('EXPECT_DATA_JSON')
        sql_data_path = read_config.get_case_file('SQL_DATA_JSON')

        # 获取的用例数据
        self.case_data_dict = read_json(case_data_path)
        self.expect_data_dict = read_json(expect_data_path)
        self.sql_data_dict = read_json(sql_data_path)

        # 加载MySQL测试用例表中的数据
        db = MysqlPool()
        self.res = db.load_table_data('test_case')


if __name__ == '__main__':
    dp = DatabaseProcessing()
    print(dp.res)

