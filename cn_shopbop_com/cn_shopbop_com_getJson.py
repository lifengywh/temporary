#! -*- coding:utf-8 -*-
# __author__ = 'lifeng@seeapp.com'
import os, sys
reload(sys)
sys.setdefaultencoding('utf8')
# os.path.abspath("../")
from cn_shopbop_com_getInfo import getInfo
import time
import gevent.monkey
gevent.monkey.patch_socket()
import gevent



#抓取商品具体信息
def url_get():
    f = open("links.txt",'r')
    url_list = f.readlines()
    f.close()
    return url_list


def fetch(url_list,pid):
    while 1:
        if len(url_list) == 0:
            break
        url = url_list[0]
        del url_list[0]
        print url,pid
        try:
            good_messages = getInfo(url.strip())
            if good_messages == 'good sold out':
                pass
            else:
                good_messages = good_messages + '\n'
                d = open('goods.txt','a')
                d.write(good_messages)
                d.close()
        except Exception,e:
            g = open('good_lose_test.txt','a')
            g.write(url)
            g.close()
            print '============================',Exception,e,url,pid

def asynchronous(url_list):
    threads = []
    for i in range(1,5):
        threads.append(gevent.spawn(fetch, url_list,i))
    gevent.joinall(threads)


if __name__ == "__main__":
    url_list = url_get()
    asynchronous(url_list)



