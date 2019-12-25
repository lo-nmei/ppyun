# coding:utf-8

import xlrd
from xlutils.copy import copy
import sys
sys.path.append("E:\\work\\python_scripts\\test_framework")
#sys.path.append("E:\\work\\python_scripts\\test_framework\\testcases")
from test_framework.base.base import *

class OperationExcel():
    #excel第一行和第一列的索引为0
    def read_excel(self, sheet_name, row):
        try:
            table = xlrd.open_workbook(filename)
            sheet = table.sheet_by_name(sheet_name)
            colx = sheet.nrows
            datalist = sheet.row_values(row, 0, colx)
            return datalist
        except Exception as f:
            print(f)
            print("读取excel文件失败")
    def read_sheet(self, sheetname):
        try:
            datalists = []
            table = xlrd.open_workbook(filename)
            sheet  = table.sheet_by_name(sheetname)
            rowx = sheet.nrows
            colx = sheet.ncols
            for i in range(1, rowx):
                if sheet.cell_value(i, 7) == "Y":
                    datalists.append(sheet.row_values(i, 0, colx))
            return datalists
        except Exception as e:
            print(e)
            print("读取excel文件失败")
        #     for i in range(row_start, row_end+1):
        #         datalists.append(self.read_excel(sheetname, i))
        #     return datalists
        # except Exception as e:
        #     print(e)
        #     print("读取excel文件失败")



    def write_excel(self, sheetname, row, value):
        try:
            table = xlrd.open_workbook(filename, formatting_info=True)
            sheet = table.sheet_by_name(sheetname)
            colx = sheet.ncols
            table_copy = copy(table)
            sheet = table_copy.get_sheet(sheetname)
            sheet.write(row, colx-1, value)
            table_copy.save(filename)
            print("test{} : 回写结果成功".format(row))
        except Exception as f:
            print(f)
            print("test{} : 回写结果失败".format(row))
    #
    def itemReplace(self, itemList, old, new):
        if isinstance(itemList, list):
            copyItemList = []
            for item in itemList:
                if isinstance(item, str):
                    item = item.replace(old, new)
                    print(item)
                copyItemList.append(item)
            return copyItemList
        else:
            raise TypeError("first argument must be list")
if __name__ == "__main__" and __package__ is None:
    __package__ = "operation_excel"
# if __name__ == "__main__":
#     url1 = "http://domain_name/api/v1/trans/mt/add"
#     url2 = "http://domain_name/api/v1/trans/mt/add111"
#     print(domain_name)
#     url1,url2 = OperationExcel().itemReplace([url1, url2], "domain_name", domain_name)
#     print(url1,url2)
print(__name__)


