import unittest

from core.basecase import BaseCase


class Test1(BaseCase):
    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

    def test03(self):
        print('test03')

    def test04(self):
        print('test04')

    def test05(self):
        print('test05')


class Test2(unittest.TestCase):
    def test011(self):
        print('test011')

    def test022(self):
        print('test022')

    def test033(self):
        print('test033')

    def test044(self):
        print('test044')

    def test055(self):
        print('test055')


# if __name__ == '__main__':
#     # 1、创建套件
#     suit = unittest.TestSuite()
#     # suit.addTest(Test("test02"))
#     # suit.addTest(Test("test01"))
#     # suit.addTests([Test('test02'), Test('test01')])
#     # 2、创建类加载的对象
#     load = unittest.TestLoader()
#     suit.addTest(load.loadTestsFromTestCase(Test1))
#     # 运行
#     run = unittest.TextTestRunner()
#     run.run(suit)

if __name__ == '__main__':
    load = unittest.TestLoader()
    suit1 = load.loadTestsFromTestCase(Test1)
    suit2 = load.loadTestsFromTestCase(Test2)
    # 指定执行类1中的一条和类2中的全部
    suits = unittest.TestSuite([Test1("test01"), suit2])
    run = unittest.TextTestRunner()
    run.run(suits)
