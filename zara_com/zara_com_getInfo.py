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



def sku_handler(color,size,price,stock,image_list):
    sku = {}
    sku["attributes"] = {}
    sku["price"] = str(price).encode("utf8")
    sku["original_price"] = str(price).encode("utf8")
    sku["images"] = image_list
    sku["stock"] = stock.encode("utf8")
    sku["attributes"]["color"] = color.encode("utf8")
    sku["attributes"]["size"] = size.encode("utf8")
    return sku

#提取图片url_list
def image_list_get(image_list):
    image_url_list = []
    for image_message in image_list:
        image_name = image_message["name"]
        image_path = image_message["path"]
        image_timestamp = image_message["timestamp"]
        image_url = ('http://static.zara.net/photos//' + image_path + '/w/1024/' + image_name + '.jpg?ts=' + image_timestamp).encode('utf8')
        image_url_list.append(image_url)
    return image_url_list



def getInfo(url):
    item = {}
    specs = []
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
    }
    print 'the good url is :',url
    r = requests.get(url,headers=header)
    soup = BeautifulSoup(r.text,'html5lib')
    title = soup.select("#description > h1")[0].get_text().strip().encode("utf8")
    sku_message = '{"product":' + soup.select("#nav-menu-container")[0].next_sibling.get_text().split('{"product":')[1][:-1].replace("true","1").replace("false","0").strip()
    sku_message = json.loads(sku_message)["product"]
    price = str(float(sku_message["price"])/100).encode('utf8')
    title = sku_message["name"].encode('utf8')
    #拼凑主要图片url
    primary_image_message = sku_message["image"]
    image_name = primary_image_message["name"] + '_1'
    image_path = primary_image_message["path"]
    image_timestamp = primary_image_message["timestamp"]
    primary_image = ('http://static.zara.net/photos//' + image_path + '/w/1024/' + image_name + '.jpg?ts=' + image_timestamp).encode('utf8')
    url = url.encode('utf8')
    #获取类别
    Category = url.split("/")[-2]
    if Category == 'view-all':
        Category = url.split("/")[-3]
    brand = ''
    desc = sku_message["description"]
    #获取image_url_list
    image_url_list_message = sku_message["xmedia"]
    image_url_list = image_list_get(image_url_list_message)

    item["original_price"] = price
    item["primary_image"] = primary_image
    item["title"] = title
    item["url"] = url
    item["category1"] = Category
    item["price"] = price
    item["brand"] = brand
    item["images"] = image_url_list
    item["desc"] = desc


    #获取sku_list
    sku_m = sku_message["detail"]["colors"]
    for c in sku_m:
        s_list = c["sizes"]
        for s in s_list:
            color = c["name"]
            size = s["name"]
            price = float(s["price"])/100
            stock = '25'
            stock_m = s["availability"]
            if stock_m == "out_of_stock":
                stock = '0'
            image_list_m = c["mainImgs"]
            image_list = image_list_get(image_list_m)
            sku = sku_handler(color,size,price,stock,image_list)
            specs.append(sku)




    result_dict = json.dumps({"items":item,"specs":specs})
    # result_dict = {"items":item,"specs":specs}
    # pprint.pprint(result_dict)
    return result_dict

if __name__ == "__main__":
    getInfo("http://www.zara.com/us/en/woman/dresses/mini/cut-out-dress-with-frills-c400009p3469538.html")





