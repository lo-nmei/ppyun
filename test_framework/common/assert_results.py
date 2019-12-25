#coding:utf-8
import unittest
class AssertResult(unittest.TestCase):
    #比较实际返回值与期望返回值
    def __init__(self):
        super(AssertResult, self).__init__()
        self.result = 1
    def compareDict(self, dict1, dict2):
        try:
            for key1, value1 in dict1.items():
                if not isinstance(value1, dict):
                    if self.assertresult(value1, dict2[key1]):
                        self.result *= 1
                    else:
                        print("{}不等于{}".format(value1, dict2[key1]))
                        self.result *= 0
                        #break
                else:
                    self.compareDict(value1, dict2[key1])
        except (AttributeError, KeyError) as e:
            print(e)
            print(dict1)
            print(dict2)
            self.result = 0
        return self.result

    def assertresult(self, res, exp_res):
        try:
            self.assertEqual(res, exp_res)
            print("pass")
            return True
        except Exception  as e:
            print("fail")
            print(e)
            return False
if __name__ == "__main__" and __package__ is None:
    __package__ = "assert_results"

if __name__ == "__main__":
    dict1 = {"content": {"sourceUrl": "as","location": "lt" },"active": True}
    dict2 = {"data": None, "err": 0, "msg": "success"}
    dict3 = {"data": None, "err": 0, "msg": "success"}
    dict4 = {"content": {"sourceUrl": "as", "location": "lt"}, "active": True}
    print(AssertResult().compareDict(dict1, dict2))