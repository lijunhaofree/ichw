#!/usr/bin/env python3

"""currency.py: It can convert the exchange rate.

__author__ = "LiJunhao"
__pkuid__  = "1800011726"
__email__  = "lijunhao@pku.edu.cn"
"""


def exchange(currency_from, currency_to, amount_from):
    lis=jstr.split('"')
    result=lis[7].split(' ')
    return result[0]                                          
    """定义一个函数可以实现汇率转化
    """

currency_from=input()
currency_to=input()
amount_from=input()
"""输入起始货币、转化货币和金额
"""

from urllib.request import urlopen  
web='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from 
doc = urlopen(web)
docstr = doc.read()
doc.close()
jstr = docstr.decode('ascii')
"""从网上提取有用的字符串"""


def test_anwser():
    assert('2.1589225'== exchange('USD','EUR',2.5))
    """测试结果是否正确
    """
def testAll():
    """test all cases"""
    test_anwser()
    print("All tests passed")
    """对所有测试函数进行调用
    """

def main():
    print(exchange(currency_from, currency_to, amount_from))
    testAll()


if __name__=='__main__':
    main()
