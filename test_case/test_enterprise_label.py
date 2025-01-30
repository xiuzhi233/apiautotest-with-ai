"""
-*- coding: utf-8 -*-
 @ Project  : apiautotest
 @ File     : test_enterprise_label.py
 @ Author   : lifuran
 @ Time     : 2024/12/22 14:42
 @ Describe : 
"""
import allure
import pytest

from common.all_datas import all_datas


class TestEnterpriseLabel:
    """
    【优化】效能 - 企业标签v1.1.0 - Web端名企分类
    飞书需求链接：https://project.feishu.cn/yupao/story/detail/4960036655
    """

    @allure.epic("【优化】效能 - 企业标签v1.1.0 - Web端名企分类")
    @pytest.mark.debug
    @pytest.mark.parametrize(
        "requirement, case_id, module, title, level, method, api, mime, data,expect, assert_type, sql_type, sql, tester",
        all_datas('4960036655'))
    def test_enterprise_label(self, req_fixture, requirement, case_id, module, title, level, method, api, mime, data,
                              expect, assert_type, sql_type, sql, tester):
        # 调用allure功能，影响报告的显示
        allure.dynamic.feature(module)
        allure.dynamic.story(api)
        allure.dynamic.title(title)
        allure.dynamic.severity(level)
        res = req_fixture.my_request(method, api, mime, data).json()
        if assert_type == "equal":
            assert res['code'] == expect['code']
        else:
            print("不支持该断言类型")


if __name__ == '__main__':
    pytest.main(['-s', '-v', '-m debug'])

    # pytest .\test_case\ --alluredir=./report/allure_json --clean-alluredir
    # allure generate .\report\allure_json\ -o .\report\allure_report
    # allure open .\report\allure_report
