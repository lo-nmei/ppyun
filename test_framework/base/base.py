#coding:utf-8
#测试环境
domain_name = "test.transsvc.ppcloud.com"
domain = "aaaaaaaaaaaaa"
headers = {"domain":domain, "Content-Type":"application/json"}
filename = "E:\\work\\python_scripts\\test_framework\\data_test\\data_test.xls"
db_config_transsvc = dict(host="10.200.9.203", port=3306, name="root", pwd="123456", database="transsvc")
db_config_transcenter = dict(host="10.200.9.203", port=3306, name="root", pwd="123456", database="transcenter")
 #根据配置文件路径读取josn文件，并反序列化为python对象，解决线上线下配置文件隔离问题
 #config = load_json("配置文件路径")
