#coding:utf-8

import pymysql
import json
class DbOperation():
    def __init__(self, host, database, name, pwd,port=3306):
        try:
            self.conn = pymysql.connect(host=host, port=port, user=name, password=pwd, database=database, charset="utf8")
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        except Exception as e:
            print(e)
            print("数据库连接失败")
    def dbsearch(self, sql):
        try:
            self.cursor.execute(sql)
            ret = self.cursor.fetchall()
        except Exception as e:
            print(e)
            print("数据库查询失败")
            ret = None
        finally:
            self.conn.close()
            return ret
    def dbModify(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            print("数据库操作失败")
            self.conn.rollback()
        finally:
            self.conn.close()
if __name__ == "__main__" and __package__ is None:
    __package__ = "db"

if __name__ == "__main__":
    # sql = """SELECT id as mtId,name,content,(case when use_watermark=0 then False else True end)use_watermark from trans_mt WHERE is_deleted=0 and domain='transsvc-82fb7515d1ce9cd45697b3cf11111111';"""
    # ret = DbOperation().dbsearch("10.200.11.40","transsvc","pplive", "123456", sql)
    # print(ret)
    # for i  in ret:
    #     i["content"] = json.loads(i["content"])
    # print(ret)
    # res = {"data":ret, "err":0, "msg":"success"}
    # # data = {"clusterId":{}, "name":{},"url":{}}
    # # for i in ret:
    # #     res["data"].append({"clusterId":i[0], "name":i[1],"url":i[2]})
    # print(res)
    DbOperation("10.200.11.40","transsvc","pplive", "123456",).dbModify("DELETE FROM trans_task WHERE mark='test';")

