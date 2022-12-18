import pytest


class Test():
    def test01(self):
        print('test1')

    @pytest.mark.smoke
    def test02(self):
        print('test2')

    def test03(self):
        print('test3')

    def test04(self):
        print('test4')
