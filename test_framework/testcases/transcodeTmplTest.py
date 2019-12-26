import unittest
import logging
from common.operation_excel import OperationExcel
from common.assert_results import AssertResult
from common.myrequests import MyRequests
from common.common import Common
from base.base  import *
from base.base import db_config_transsvc as db
from testcases.subunittest import SubUnittest
from common.db import DbOperation
import requests
import json
import ddt
@ddt.ddt
class TestTmplAdd(SubUnittest):
    data_lists = OperationExcel().read_sheet("transcode_template_add")
    data_lists.pop(0)
    skipmsg = 1
    def setUp(self):
        setUpDataList = OperationExcel().read_sheet("transcode_template_add").pop(0)
        data = setUpDataList[4]
        self.mtId = self.initMt(data)
    @ddt.data(*data_lists)
    @ddt.unpack
    @unittest.skipIf(skipmsg == 0, "调试别的用例")
    def test_tmplAdd(self, id, descrition, method, url, data=None, expect_res=None, actual_res=None, run=None, result=None):
        url = url.replace("domain_name", domain_name)
        data = data.replace("mtId待定", str(self.mtId))
        expect_res = json.loads(expect_res)
        res = MyRequests(method, url, data=data, headers=headers).myrequests()
        if res["msg"] == "success":
            expect_res["data"]["tmplId"] = res["data"]["tmplId"]
            if res["data"] != None:
                self.tmplId = res["data"]["tmplId"]
        else:
            self.tmplId = 0
        if AssertResult().compareDict(res, expect_res):
            OperationExcel().write_excel("transcode_template_add", id, "pass")
        else:
            OperationExcel().write_excel("transcode_template_add", id, "fail")
    def tearDown(self):
        #删除档位模板
        self.clearTranscodeTmpl(self.mtId, self.tmplId)

#转码模板修改/删除/查询/测试
@ddt.ddt
class TestTmplOperation(SubUnittest):
    data_lists = OperationExcel().read_sheet("transcode_tempalte_operation")
    data_lists.pop(0)
    data_lists.pop(0)
    skipmsg = 1
    def setUp(self):
        setUpDataLists = OperationExcel().read_sheet("transcode_tempalte_operation")
        mt_data = setUpDataLists.pop(0)[4]
        self.mtId = self.initMt(mt_data)
        tmpl_data = setUpDataLists.pop(0)[4].replace("mtId待定", str(self.mtId))
        self.tmplId = self.initTmpl(tmpl_data)
    @ddt.data(*data_lists)
    @ddt.unpack
    @unittest.skipIf(skipmsg == 0, "调试别的用例")
    def test_tmplOperation(self, id, descrition, method, url, data=None, expect_res=None, actual_res=None, run=None, sql=None, result=None):
        url, data, expect_res = Common().itemReplace([url, data, expect_res], "tmplId待定", str(self.tmplId))
        url, data, expect_res = Common().itemReplace([url, data, expect_res], "mtId待定", str(self.mtId))
        url = Common().itemReplace([url], "domain_name", domain_name)
        expect_res = json.loads(expect_res)
        res = MyRequests(method, url, data=data, headers=headers).myrequests()
        if AssertResult().compareDict(res, expect_res):
            OperationExcel().write_excel("transcode_tempalte_operation", id, "pass")
        else:
            OperationExcel().write_excel("transcode_tempalte_operation", id, "fail")
    def tearDown(self):
        self.clearTranscodeTmpl(self.mtId, self.tmplId)
@ddt.ddt
class TestTransTmplSearch(SubUnittest):
    data_lists = OperationExcel().read_excel("transcode_tempalte_operation", 6)
    def setUp(self):
        print("test begin")
    @ddt.data(data_lists)
    @ddt.unpack
    def test_tmplSearch(self, id, descrition, method, url, data=None, expect_res=None, actual_res=None, run=None, sql=None, result=None):
        sqlData = DbOperation(db["host"], db["database"], db["name"], db["pwd"]).dbsearch(sql)
        url = Common().itemReplace([url], "domain_name", domain_name)
        expect_res = json.loads(expect_res)
        for i in sqlData:
            if i["mtList"]:
                i["mtList"] = [int(j) for j in i["mtList"].split(",")]
        res = MyRequests(method, url, data=data, headers=headers).myrequests()
        expect_res["data"] = list(sqlData)
        if AssertResult().compareDict(res, expect_res):
            OperationExcel().write_excel("transcode_tempalte_operation", id, "pass")
        else:
            OperationExcel().write_excel("transcode_tempalte_operation", id, "fail")
    def tearDown(self):
        print("test done")


if __name__ == "__main__":
    unittest.main()
