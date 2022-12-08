"""
自定义日志
1. 控制台输出
2. 运行日志记录到文件中
https://docs.python.org/3/howto/logging-cookbook.html
https://docs.python.org/3/library/logging.html#logging.LogRecord
"""

import logging
import os

logger = logging.getLogger("testapi")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
# 控制台输出处理器
sh = logging.StreamHandler()
sh.setFormatter(formatter)
# 日志级别
sh.setLevel(logging.DEBUG)
# 添加控制台输出
logger.addHandler(sh)

# 定义日志存放文件路径
logs = os.path.join(os.path.dirname(__file__),'../logs')
if not os.path.exists(logs):
    os.mkdir(logs)
logfile = os.path.join(logs,'apilog.log')
fh = logging.FileHandler(logfile)
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)

logger.addHandler(fh)

if __name__ == '__main__':
    logger.info("this is test")