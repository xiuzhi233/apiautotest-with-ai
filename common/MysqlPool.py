"""
-*- coding: utf-8 -*-
 @ Project  : apiautotest
 @ File     : MysqlPool.py
 @ Author   : lifuran
 @ Time     : 2024/12/20 10:22
 @ Describe : 
"""
import pymysql
from dbutils.pooled_db import PooledDB
from common.ReadConfig import ReadConfig


class MysqlPool:
    # 连接池对象
    __pool = None
    read_ini = ReadConfig()

    def __init__(self):

        self._connection = self.__get_connection()
        self._cursor = self._connection.cursor()

    def __get_connection(self):
        """
        从连接池获取连接
        :return:
        """
        if self.__pool is None:
            __pool = PooledDB(creator=pymysql,
                              mincached=int(self.read_ini.get_mysql_connection("DB_POOL_MIN_CONN")),
                              maxcached=int(self.read_ini.get_mysql_connection("DB_POOL_MAX_CONN")),
                              host=self.read_ini.get_mysql_connection("MYSQL_HOST"),
                              port=int(self.read_ini.get_mysql_connection("MYSQL_PORT")),
                              user=self.read_ini.get_mysql_connection("MYSQL_USER"),
                              passwd=self.read_ini.get_mysql_connection("MYSQL_PASSWORD"),
                              db=self.read_ini.get_mysql_connection("MYSQL_DATABASE"),
                              use_unicode=True,
                              charset=self.read_ini.get_mysql_connection("MYSQL_CHARSET"),
                              cursorclass=pymysql.cursors.DictCursor)
            return __pool.connection()

    def load_table_data(self, table_name):
        """
        从指定的 MySQL 表中加载所有数据，并返回一个二维列表。
        :param table_name:
        :return:
        """
        data = list()

        query = f"SELECT * FROM {table_name}"

        try:
            # 执行查询
            self._cursor.execute(query)

            # 获取所有结果
            results = self._cursor.fetchall()

            # 将结果转换为二维列表
            data = [list(row.values()) for row in results]
        except Exception as err:
            print(f"查询失败: {err}")
        return data

    def select(self, sql_sentence):
        """
        执行查找的sql语句
        :param sql_sentence: sql语句
        :return:查询的结果
        """
        try:
            # 使用游标对象执行sql语句
            self._cursor.execute(sql_sentence)

        except ValueError:
            raise ValueError("请确认sql语句是否正确！")

        else:
            # 接收查询的结果
            select_result = self._cursor.fetchall()
            # 判断查询结果是否有数据
            if select_result:
                return select_result[0][0]
            else:
                return None

    def delete(self, sql_sentence):
        """执行删除的sql语句"""
        try:
            # 使用游标对象执行sql语句
            self._cursor.execute(sql_sentence)

        except ValueError:
            raise ValueError("请确认sql语句是否正确！")

        else:
            # 使用游标对象提交
            self._connection.commit()

    # 从连接池中取出一个连接
    def getconn(self):
        self._connection = self.__get_connection()
        self._cursor = self._connection.cursor()

    def begin(self):
        """
        @summary: 开启事务
        """
        self._connection.autocommit(0)

    def end(self, option='commit'):
        """
        @summary: 结束事务
        """
        if option == 'commit':
            self._connection.commit()
        else:
            self._connection.rollback()

    def dispose(self, is_end=1):
        """
        @summary: 释放连接池资源
        """
        if is_end == 1:
            self.end('commit')
        else:
            self.end('rollback')
        self._cursor.close()
        self._connection.close()


if __name__ == '__main__':
    mp = MysqlPool()
    print(mp.load_table_data("test_case"))
    mp.dispose()
