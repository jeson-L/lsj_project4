import allure


def allure_init(requests_data):
    allure.dynamic.feature(requests_data['module'])
    allure.dynamic.story(requests_data['story'])
