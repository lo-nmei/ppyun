#from ..testcases import function_test
import unittest
import os
import sys
from BeautifulReport import  BeautifulReport as bf
import time
from tomorrow3 import threads
top_path = os.path.abspath("..")
print(top_path)
sys.path.append(top_path)
# from testcases.logoTemplateTest import *
caces_path = os.path.join(top_path, "testcases")
log_path = os.path.join(top_path, "report")
filename = "report-" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
print(filename)
rule = "logoTemplateTest.py"
sys.stdout.flush()
# runner = unittest.TextTestRunner()
# runner.run(discover)
def add_case(rule):
    cases = unittest.defaultTestLoader.discover(caces_path, pattern = rule, top_level_dir=None)
    return cases
@threads(5)
def run(cases):
    runner = bf(cases)
    runner.report(filename=filename, description="多线程测试", dir_path = log_path)

if __name__ == "__main__":
    for i in add_case("logoTemplateTest.py"):
        run(i)

