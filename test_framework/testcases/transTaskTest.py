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
class test_taskAdd(SubUnittest):
    data_lists = OperationExcel().read_sheet("task_add")
    def setUp(self):
        print("begin test")
    @ddt.data(*data_lists)
    @ddt.unpack
    def test_taskAdd(self, id, descrition, method, url, data, expect_res, actual_res=None, run=None, sql=None, result=None):
        url = Common().itemReplace([url], "domain_name", domain_name)
        res = MyRequests(method, url, data=data, headers=headers).myrequests()
        sqldata = DbOperation(db["host"], db["database"], db["name"], db["pwd"]).dbsearch(sql)
        self.taskId = sqldata[0]["taskId"]
        expect_res = json.loads(expect_res)
        expect_res["data"]["taskId"] = self.taskId
        if AssertResult().compareDict(res, expect_res):
            OperationExcel().write_excel("task_add", id, "pass")
        else:
            OperationExcel().write_excel("task_add", id, "fail")
    def tearDown(self):
        DbOperation(db["host"], db["database"], db["name"], db["pwd"]).dbModify("DELETE FROM trans_task WHERE mark='test';")
        print("test done")
