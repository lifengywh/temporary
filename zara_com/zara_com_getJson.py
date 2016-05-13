#! -*- coding:utf-8 -*-
# __author__ = 'lifeng@seeapp.com'
import os, sys
reload(sys)
sys.setdefaultencoding('utf8')
# os.path.abspath("../")
from zara_com_getInfo import getInfo
import time



#抓取商品具体信息
def main():
    f = open("link.txt",'r')
    url_list =  f.readlines()
    f.close()
    a = 12146
    for ff in url_list[12146:]:
        print ff
        print a
        a += 1
        try:
            good_messages = getInfo(ff.strip())
            good_messages = good_messages + '\n'
            d = open('goods.txt','a')
            d.write(good_messages)
            d.close()
        except Exception,e:
            g = open('good_lose.txt','a')
            g.write(ff)
            g.close()
            time.sleep(10)
            print '============================',Exception,e

if __name__ == "__main__":
    main()


