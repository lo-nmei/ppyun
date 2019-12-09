# coding:utf-8
import time
import datetime
import os
import requests
import pymysql
class RunStatistics():
    #duration = -29
    def __init__(self, duration):
        self.start_date = ""
        self.end_date = ""
        self.sql = ""
        self.db_result = None
        self.search_result = None
        self.duration = duration
    def create_time(self):
        origin_end_time = datetime.date.today() + datetime.timedelta(days=+1)
        origin_start_time = datetime.date.today() + datetime.timedelta(days=self.duration)
        self.end_date = origin_end_time.strftime("%Y%m%d")
        self.start_date = origin_start_time.strftime("%Y%m%d")
        self.sql = "SELECT count(1) as taskNum from trans_task WHERE created_time>'{} 00:00:00' and created_time<'{} 00:00:00' and (is_deleted=0 or (is_deleted=1 and `status`='successed')) and `status` in ('successed','failed')".format(origin_start_time.strftime("%Y-%m-%d"), origin_end_time.strftime("%Y-%m-%d"))
        print(self.sql)
        print(origin_start_time, origin_end_time)
    def run_case(self):
        url = "http://test.transsvc.ppcloud.com/private/trans/task/statis?domain=global&startDate={}&endDate={}".format(self.start_date, self.end_date)
        result = requests.get(url)
        self.search_result = result.json()["data"][0]["summary"]["taskNum"]
        # print(self.search_result)
    def db_opration(self, host, database, name, pwd, port=3306):
        try:
            conn = pymysql.connect(host=host, database=database, user=name, password=pwd, port=port, cursorclass=pymysql.cursors.DictCursor)
            cursor = conn.cursor()
            try:
                cursor.execute(self.sql)
                ret = cursor.fetchall()
            except Exception as e:
                print(e)
                print("数据库查询失败")
                ret = None
            finally:
                conn.close()
        except Exception as e:
            ret = None
            print(e)
            print("数据库连接失败")
        if ret:
            self.db_result = ret[0]["taskNum"]
        else:
            self.db_result = ret
    def check_result(self):
        print("接口查询总量：{}".format(self.search_result))
        print("数据库查询总量：{}".format(self.db_result))
        if self.db_result == self.search_result:
            print("统计结果与数据库一致 通过")
        else:
            print("统计结果与数据库不一致 失败")

if __name__ == "__main__":
    for i in range(-29, 1):
        runcases = RunStatistics(i)
        runcases.create_time()
        runcases.run_case()
        runcases.db_opration("10.200.9.203", "transsvc", "root", "123456")
        runcases.check_result()


