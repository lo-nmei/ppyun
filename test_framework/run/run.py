#from ..testcases import function_test
import unittest
import os
import sys
from BeautifulReport import  BeautifulReport as bf
import time
from test_framework.testcases.logoTemplateTest import *
top_path = os.path.abspath("..")
sys.path.append(top_path)
caces_path = os.path.join(top_path, "testcases")
log_path = os.path.join(top_path, "report")
filename = "report-" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
print(filename)
discover = unittest.defaultTestLoader.discover(caces_path, pattern = "logoTemplateTest.py", top_level_dir=None)
sys.stdout.flush()
# runner = unittest.TextTestRunner()
# runner.run(discover)
run = bf(discover)
run.report(filename=filename, description="报告描述参数", report_dir=log_path)