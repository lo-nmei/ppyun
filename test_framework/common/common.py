# coding:utf-8
import sys
sys.path.append("E:\\work\\python_scripts\\test_framework")
sys.path.append("E:\\work\\python_scripts\\test_framework\\testcases")
from test_framework.base.base import *
class Common():
    def itemReplace(self, itemList, old, new):
        if isinstance(itemList, list):
            copyItemList = []
            for item in itemList:
                if isinstance(item, str):
                    item = item.replace(old, new)
                copyItemList.append(item)
            if len(copyItemList) == 1:
                return copyItemList[0]
            else:
                return copyItemList
        else:
            raise TypeError("first argument must be list")
if __name__ == "__main__" and __package__ is None:
    __package__ = "common"


if __name__ == "__main__":
    url1 = "http://domain_name/api/v1/trans/mt/add"
    url2 = "http://domain_name/api/v1/trans/mt/add111"
    print(domain_name)
    url1 = Common().itemReplace([url1], "domain_name", domain_name)
    print(url1)