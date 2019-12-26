import unittest
import logging
from common.operation_excel import OperationExcel
from common.assert_results import AssertResult
from common.myrequests import MyRequests
from base.base  import *
import requests
import json
import ddt
#unittest.TestCase的子类，添加了方法
class SubUnittest(unittest.TestCase):
    #初始化档位模板
    def initMt(self, data):
        method = "post"
        url = "http://{}/api/v1/trans/mt/add".format(domain_name)
        res = MyRequests(method, url, data=data, headers=headers).myrequests()
        if res["msg"] == "success":
            mtId = res["data"]["mtId"]
            print("档位模板初始化成功")
        else:
            mtId = 0
            print("档位模板初始化失败")
        return mtId
    #初始化转码模板
    def initTmpl(self, data):
        method = "post"
        url = "http://{}/api/v1/trans/tmpl/add".format(domain_name)
        res = MyRequests(method, url, data=data, headers=headers).myrequests()
        if res["msg"] == "success":
            tmplId = res["data"]["tmplId"]
            print("转码模板初始化成功")
        else:
            tmplId = 0
            print("转码模板初始化失败")
        return tmplId
    #删除测试档位模板和转码模板
    def clearTranscodeTmpl(self, mtId, tmplId):
        if tmplId != 0:
            method = "post"
            url_tmpl = "http://{}/api/v1/trans/tmpl/delete?tmplId={}".format(domain_name, tmplId)
            res = MyRequests(method, url_tmpl, headers=headers).myrequests()
            if res["msg"] == "success":
                print("删除转码模板成功")
            else:
                print("删除转码模板失败或转码模板已被删除")
        else:
            print("不需要删除转码模板")
        self.clearMt(mtId)
    #删除测试档位模板
    def clearMt(self, mtId):
        print("******************")
        print("mtId : {}".format(mtId))
        if mtId != 0:
            method = "post"
            url_mt = "http://{}/api/v1/trans/mt/delete?mtId={}".format(domain_name, mtId)
            res = MyRequests(method, url_mt, headers=headers).myrequests()
            print(res)
            if res["msg"] == "success":
                print("删除档位模板成功")
            else:
                print("删除档位模板失败或档位模板已被删除")
        else:
            print("不需要删除档位模板")
    def itemReplace(self, itemList, old, new):
        for item in itemList:
            if isinstance(item, str):
                item = item.replace(old, new)

if __name__ == "__main__":
    url = "http://domain_name/api/v1/trans/mt/add"
    print(1)
    SubUnittest().itemReplace(url, "domain_name", domain_name)
    print(url)



