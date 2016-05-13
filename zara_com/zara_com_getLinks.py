#! -*- coding:utf-8 -*-
# __author__ = 'lifeng@seeapp.com'
import os, sys, getopt
reload(sys)
sys.setdefaultencoding('utf8')
import requests
from bs4 import BeautifulSoup
import json
import pprint
import re



#获取大类
def getLink():
    cate_all_list = []
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
    }
    start_url = "http://www.zara.com/us/"
    print start_url
    r = requests.get(start_url,headers=header)
    soup = BeautifulSoup(r.text,'html5lib')
    cate_list = soup.select("#menu > ul > li > a")
    #抓取大类
    for cate in cate_list:
        cate_name = cate.get_text()
        if cate_name in ["WOMAN","TRF","KIDS"]:
            cate_url = cate["href"]
            cate_all_list.append(cate_url)
            #抓取小类
            cate_min_list = cate.next_sibling.find_all("a")
            for cate_min in cate_min_list:
                cate_min_url = cate_min["href"]
                cate_all_list.append(cate_min_url)
    print 'the cate_all_list num is:',len(cate_all_list)
    
    #提取商品url
    for url in cate_all_list[:2]:
    # for url in cate_all_list:
        print 'the cate url is ',url
        r1 = requests.get(url,headers=header)
        soup1 = BeautifulSoup(r1.text,"html5lib")
        good_list = soup1.select("#products > ul > li > a")
        for good in good_list:
            good_url = "http:" + good["href"]
            print good_url
            
        
    


getLink()

