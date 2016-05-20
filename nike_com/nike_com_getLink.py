#! -*- coding:utf-8 -*-
# __author__ = 'lifeng@seeapp.com'
import os, sys, getopt
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import time
import logging,logging.handlers
from bs4 import BeautifulSoup
import json
import pprint
import re
import math



def good_url_get(url,header):
    r = requests.get(url,headers=header)
    soup = BeautifulSoup(r.text,'html5lib')
    goods_url_list = soup.select(".category-products > ul > li")
    for g in goods_url_list:
        good_url = g.a["href"] + '\n'
        f = open("links.txt",'a')
        f.write(good_url)
        f.close()


def getLink():
    header ={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
    }
    start_url = 'http://www.nike.com'
    r = requests.get(start_url,headers=header)
    # soup = BeautifulSoup(r.text,'html5lib')

    f = open('test.html','w')
    f.write(r.text)
    f.close()




getLink()



