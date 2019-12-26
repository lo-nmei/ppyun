import unittest
import logging
from common.operation_excel import OperationExcel
from common.assert_results import AssertResult
from common.myrequests import MyRequests
from common.db import DbOperation
from base.base  import *
from base.base import db_config_transsvc as db
from common.common import Common
from testcases.subunittest import SubUnittest
import requests
import json
import ddt
@ddt.ddt
class TestCluster(SubUnittest):
    data_lists = OperationExcel().read_sheet("cluster_search")
    def setUp(self):
        print("begin test")
    @ddt.data(*data_lists)
    @ddt.unpack
    def test_cluster(self, id, descrition, method, url, data, expect_res, actual_res=None, run=None, sql=None, result=None):
        url = Common().itemReplace([url], "domain_name", domain_name)
        res = MyRequests(method, url, data=data, headers=headers).myrequests()
        resData = DbOperation(db_config_transsvc["host"], db_config_transsvc["database"], db_config_transsvc["name"], db_config_transsvc["pwd"]).dbsearch( sql)
        expect_res = json.loads(expect_res)
        expect_res["data"] = resData
        print(res)
        if AssertResult().compareDict(res, expect_res):
            OperationExcel().write_excel("cluster_search", id, "pass")
        else:
            OperationExcel().write_excel("cluster_search", id, "fail")
    def tearDown(self):
        print("test done")

if __name__ == "__main__":
    unittest.main()
