import os
import sys
#sys.path.append(os.path.abspath("E:\\work\\python_scripts\\test_framework"))
import unittest
from BeautifulReport import  BeautifulReport as bf
import logging
from test_framework.common.operation_excel import OperationExcel
from test_framework.common.assert_results import AssertResult
from test_framework.common.myrequests import MyRequests
from test_framework.base.base  import *
import requests
import json
import ddt


@ddt.ddt
class TestLogo(unittest.TestCase):
    #excel的行和列从0开始计数
    data_lists = OperationExcel().read_sheet("logo_template_save")
    skipReason = 1
    @classmethod
    def setUpClass(cls):
        print("begin test of logo_template_save")
    @ddt.data(*data_lists)
    @unittest.skipIf(skipReason == 0, "调试别的用例")
    def test_logo(self, datalist):
        """水印模板保存"""
        logging.info("begin read data_test")
        method = datalist[2]
        id = datalist[0]
        description = datalist[1]
        url = datalist[3].replace("domain_name", domain_name)
        data = json.dumps(eval(datalist[4]))
        expect_res = datalist[5]
        #headers = {"domain":domain, "Content-Type":"application/json"}
        res = MyRequests(method, url, headers = headers, data = data).myrequests()
        res = json.dumps(res)
            #print(res)
        if AssertResult().assertresult(res, expect_res):
            OperationExcel().write_excel("logo_template_save", id, "pass")
        else:
            OperationExcel().write_excel("logo_template_save", id, "fail")
    @classmethod
    def tearDownClass(cls):
        print("test of logo_tempalte_save is done")
@ddt.ddt
class LogoSearch(unittest.TestCase):
    datalist = OperationExcel().read_sheet("logo_template_search")
    datalist.pop(0)
    setupres = 1
    #print("**********\n")
    #print(datalist)
    def setUp(self):
        setUpDataList = OperationExcel().read_sheet("logo_template_search").pop(0)
        method = setUpDataList[2]
        url = setUpDataList[3].replace("domain_name", domain_name)
        data = setUpDataList[4]
        expect_res = setUpDataList[5]
        expect_res_dict = json.loads(expect_res)
        setUpRes = MyRequests(method, url, headers = headers, data = data).myrequests()
        #setUpRes = json.dumps(setUpRes)
        if not AssertResult().compareDict(setUpRes, expect_res_dict):
            print("初始化水印模板失败")
            setupres = 1
        else:
            print("初始化水印模板成功\n")
            setupres = 0
    @ddt.data(*datalist)
    @unittest.skipIf(setupres == 0, "水印模板初始化失败")
    def test_logo_search(self, datalist):
        """水印模板查询"""
        id = datalist[0]
        method = datalist[2]
        url = datalist[3].replace("domain_name", domain_name)
        expect_res = json.loads(datalist[5])
        res = MyRequests(method, url, headers = headers).myrequests()
        #res = json.dumps(res)
            #print(res)
        if AssertResult().compareDict(res, expect_res):
            OperationExcel().write_excel("logo_template_search", id, "pass")
        else:
            OperationExcel().write_excel("logo_template_search", id, "fail")
    def tearDown(self):
        print("水印模板查询完成")


# suit = unittest.TestSuite()
# suit.addTest(unittest.makeSuite(TestLogo))
# run = bf(suit)
# run.report(filename="test", description="水印模板保存")

# if __name__ == '__main__':
# #     suit = unittest.TestSuite()
# #     suit.addTest(unittest.makeSuite(TestLogo))
# #     run = bf(suit)
# #     run.report(filename="test", description="水印模板保存")
