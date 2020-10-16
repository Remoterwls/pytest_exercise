#!/bash/bin/env
# -*- coding:utf8 -*-

# __author__: jack wu


import pytest
from calculator import Calc



class TestCalc:
    """
        test calculator's function
    """

    def setup_class(self):
        print('开始计算')
        self.cc = Calc()

    def teardown_class(self):
        print('结束计算')

    @pytest.mark.parametrize('a,b,expect',[[1,2,3],[1,0,1],[100,200,300],[-1,-2,-3],[0.1,1,1.1],[0.3,0.6,0.9]])
    def test_add(self,a,b,expect):
        result = self.cc.add(a,b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',[(1,2,-1),(1,1,0),(2,1,1),(-1,-1,0)])
    def test_minus(self,a,b,expect):
        result = self.cc.minus(a,b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [(1, 2, 2), (1, 1, 1), (0, 2, 0), (-1, -1, 1),(-10,10,-100),(0.1,0.2,0.02)])
    def test_multiple(self,a,b,expect):
        result = self.cc.multiple(a,b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',[[1,1,1],[1,2,0.5],[4,2,2],[0,4,0]])
    def test_divide(self,a,b,expect):
        result = self.cc.divide(a,b)
        assert result == expect


    def test_divide_divisor_is_zero(self,a=1,b=0):
        result = self.cc.divide(a,b)
        assert result == '除数不能为零'




if __name__ == '__main__':
    pytest.main(['-s',''])

