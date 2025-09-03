import openpyxl

from config.config import FILEPATH, SHEET_NAME


def read_excel():
    workbook = openpyxl.load_workbook(FILEPATH)
    sheet = workbook[SHEET_NAME]
    # 存放所有的参数字段名
    keys = []
    # 存放所有测试用例的请求参数
    datas = []

    # 拿取所有的请求参数头
    for cell in sheet[2]:
        keys.append(cell.value)

    # 拿取所有用例的请求参数
    for row in list(sheet.iter_rows(min_row=3, values_only=True)):
        if dict(zip(keys, row))['is_true']:
            datas.append(dict(zip(keys, row)))

    # 关闭excel
    workbook.close()
    return datas
