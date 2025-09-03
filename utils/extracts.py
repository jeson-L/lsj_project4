import logging

import jsonpath
from utils.http_requests import jdbc_select_requests


def json_extract(requests_data, res, all):
    # json提取
    if requests_data['json_extract']:
        for key, value in eval(requests_data['json_extract']).items():
            all[key] = jsonpath.jsonpath(res.json(), expr=value)[0]
            logging.info('根据响应结果({})---提取出的数据是：---({})'.format(res.json(),all[key]))


# 数据库提取
def sql_extract(requests_data, all):
    if requests_data['sql_extract']:
        for key, value in eval(requests_data['sql_extract']).items():
            all[key] = jdbc_select_requests(value)
            logging.info('根据sql({})提取出的数据是：({})'.format(requests_data['sql_extract'], all[key]))

