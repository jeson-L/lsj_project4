import pytest
import requests

from utils.allure_init import allure_init
from utils.asserts import http_assert, sql_assert
from utils.extracts import json_extract, sql_extract
from utils.http_requests import http_requests
from utils.parsing_data import parsing_data
from utils.read_excel import read_excel


class TestCase:
    # 全局变量存放
    all_element = {}
    datas = read_excel()

    @pytest.mark.parametrize('data', datas)
    def testcases(self, data):
        all = self.all_element

        # 赋值，不然会报错
        requests_data = data

        # 解析数据
        request_data = parsing_data(requests_data, all)

        # allure初始化报告
        allure_init(requests_data)

        # 发送http请求
        res = http_requests(request_data)

        # json提取
        json_extract(requests_data, res, all)

        # 数据库提取
        sql_extract(requests_data, all)

        # 数据库断言
        sql_assert(requests_data)

        # HTTP响应断言
        http_assert(requests_data, res)
