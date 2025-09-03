import jinja2
import logging

from config.config import PATH


# @allure.step('请求参数：')
def parsing_data(requests_data, all):
    method = requests_data['method']
    url = PATH + jinja2.Template(requests_data['path']).render(all)
    data = eval(jinja2.Template(requests_data['data']).render(all)) if isinstance(requests_data['data'], str) else None
    params = eval(requests_data['params']) if isinstance(requests_data['params'], str) else None
    json = eval(requests_data['json']) if isinstance(requests_data['json'], str) else None
    files = eval(requests_data['files']) if isinstance(requests_data['files'], str) else None
    headers = eval(jinja2.Template(requests_data['headers']).render(all)) if isinstance(requests_data['headers'],
                                                                                        str) else None

    request_data = {
        "method": method,
        "url": url,
        "params": params,
        "data": data,
        "json": json,
        "files": files,
        "headers": headers
    }
    logging.info("用例标题: {}".format(requests_data['title']))
    logging.info("请求参数:{}".format(request_data))
    return request_data
