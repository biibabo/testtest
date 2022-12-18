import unittest
import HTMLTestRunner
test_dir = "E:/Program Files/testtest/testdemo"
report_path = "E:/Program Files/testtest/report/report"
# wb:二进制写入
# 打开目录生成html文件
file = open(report_path + "-result.html", "wb")

# 文件格式生成
run = HTMLTestRunner.HTMLTestRunner(stream=file, title="这是报告的标题", description="这是描述")

# 加载用例
dis = unittest.defaultTestLoader.discover(test_dir, pattern='testdemo_*.py')

# suit = unittest.TestSuite()
# suit.addTest(dis)
#
# run = unittest.TextTestRunner()
# run.run(suit)
# 运行用例
run.run(dis)