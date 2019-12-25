import unittest
import logging
from ..common.operation_excel import OperationExcel
from ..common.assert_results import AssertResult
from ..common.myrequests import MyRequests
from ..base.base  import *
from .subunittest import SubUnittest
from ..base.base import db_config_transsvc as db
from ..common.db import DbOperation
from ..common.common import Common
import json
import ddt
@ddt.ddt
class TestMtAdd(SubUnittest):
    data_lists = OperationExcel().read_sheet("mt_template_add")
    skipmsg = 1
    def setUp(self):
        print("begin test of mt_tempalte")
    @ddt.data(*data_lists)
    @ddt.unpack
    @unittest.skipIf(skipmsg == 0, "调试别的用例")
    def test_mt(self, id, descrition, method, url, data, expect_res, actual_res=None, run=None, sql=None, result=None):
        #print(descrition)
        url = url.replace("domain_name", domain_name)
        res = MyRequests(method, url, data=data, headers=headers).myrequests()
        expect_res = json.loads(expect_res)
        #print(res)
        #print(res["data"]["mtId"])

        if res["msg"] == "success":
            self.mtId = res["data"]["mtId"]
            if expect_res["data"] != None:
                expect_res["data"]["mtId"] = res["data"]["mtId"]
        else:
            self.mtId = 0
        if descrition == "档位模板/新增/name已存在":
            res = MyRequests(method, url, data=data, headers=headers).myrequests()
        if AssertResult().compareDict(res, expect_res):
            OperationExcel().write_excel("mt_template_add", id, "pass")
        else:
            OperationExcel().write_excel("mt_template_add", id, "fail")
    def tearDown(self):
        self.clearMt(self.mtId)
@ddt.ddt
class TestMtOperation(SubUnittest):
    data_lists = OperationExcel().read_sheet("mt_tempalte_opteration")
    data_lists.pop(0)
    skipmsg = 1
    def setUp(self):
        setUpDataList = OperationExcel().read_sheet("mt_tempalte_opteration").pop(0)
        data = setUpDataList[4]
        self.mtId = self.initMt(data)
    @ddt.data(*data_lists)
    @ddt.unpack
    @unittest.skipIf(skipmsg == 0, "调试别的用例")
    def test_mtOperate(self, id, descrition, method, url, data=None, expect_res=None, actual_res=None, run=None, sql=None, result=None):
        url = url.replace("domain_name", domain_name)
        url = url.replace("mtId待定", str(self.mtId))
        if data != None:
            data = data.replace("mtId待定", str(self.mtId))
        expect_res = expect_res.replace("mtId待定", str(self.mtId))
        res = MyRequests(method, url, data=data, headers=headers).myrequests()
        expect_res = json.loads(expect_res)
        # print(res["data"]["mtId"])
        if descrition == "档位模板/删除/异常":
            res = MyRequests(method, url, data=data, headers=headers).myrequests()
        if AssertResult().compareDict(res, expect_res):
            OperationExcel().write_excel("mt_tempalte_opteration", id, "pass")
        else:
            OperationExcel().write_excel("mt_tempalte_opteration", id, "fail")
    def tearDown(self):
        self.clearMt(self.mtId)
@ddt.ddt
class TestMtSearch(SubUnittest):
    data_lists = OperationExcel().read_excel("mt_tempalte_opteration", 7)
    def setUp(self):
        print("begin test")
    @ddt.data(data_lists)
    @ddt.unpack
    def test_mtSearch(self, id, descrition, method, url, data=None, expect_res=None, actual_res=None, run=None, sql=None, result=None):
        url = Common().itemReplace([url], "domain_name", domain_name)
        expect_res = json.loads(expect_res)
        sqlData = DbOperation(db["host"], db["database"], db["name"], db["pwd"]).dbsearch(sql)
        for i in sqlData:
            i["content"] = json.loads(i["content"])
        expect_res["data"] = sqlData
        res = MyRequests(method, url, data=data, headers=headers).myrequests()
        # print(res)
        # print(expect_res)
        if AssertResult().compareDict(res, expect_res):
            OperationExcel().write_excel("mt_tempalte_opteration", id, "pass")
        else:
            OperationExcel().write_excel("mt_tempalte_opteration", id, "fail")
    def tearDown(self):
        print("test done")

if __name__ == "__main__":
    unittest.main()