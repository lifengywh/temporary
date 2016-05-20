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


def sku_handler(color,size,price,original_price,stock,image_list):
    sku = {}
    sku["attributes"] = {}
    sku["price"] = str(price).encode("utf8")
    sku["original_price"] = str(original_price).encode("utf8")
    sku["images"] = image_list
    sku["stock"] = stock.encode("utf8")
    sku["attributes"]["color"] = color.encode("utf8")
    sku["attributes"]["size"] = size.encode("utf8")
    return sku

#提取图片url_list
def image_list_get(image_list):
    image_url_list = []
    for k,v in image_list.items():
        image_url = v["zoom"]
        image_url_list.append(image_url)
    return image_url_list

#color id 转换为color
def size_get(sku_size,size_id):
    for k,v in sku_size.items():
        if v["sizeCode"] == size_id:
            return k


def getInfo(url):
    item = {}
    specs = []
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
    }
    print 'the good url is :',url
    r = requests.get(url,headers=header)
    soup = BeautifulSoup(r.text,'html5lib')
    #提取价格
    price_message = soup.select("#productPrices")[0].select(".priceBlock")
    original_price = price_message[0].get_text().split('$')[1].strip().encode('utf8')
    price = original_price
    if len(price_message) == 2:
        try:
            price = price_message[1].select(".salePrice")[0].get_text().split('$')[1].strip().encode('utf8')
        except:
            price = price_message[1].select(".salePrice")[1].get_text().split('$')[1].strip().encode('utf8')

    try:
        Category = soup.select(".breadcrumb > a > span")[0].get_text().strip().encode('utf8')
    except:
        Category = soup.select(".breadcrumb > span")[0].get_text().strip().encode('utf8')
    try:
        brand = soup.select(".brand-heading > div > a")[0].get_text().strip().encode('utf8')
    except:
        brand = soup.select(".brand-heading > div")[0].get_text().strip().encode('utf8')
    title = soup.select(".brand-heading > span")[0].get_text().strip().encode('utf8')
    url = url.encode('utf8')
    desc = soup.select("#detailsAccordion > div")[0].get_text().strip().encode('utf8')

    sku_message = soup.select("#designersThickBoxcontainer")[0].next_sibling.next_sibling.get_text().split("productDetail=")[1].split("var productPage=")[0].strip()[:-1]
    sku_message = json.loads(sku_message)
    # pprint.pprint(sku_message)
    if sku_message["sizes"] == {}:
        return 'good sold out'
    for k,v in sku_message["colors"].items():
        for size in sku_message["sizes"]:
            color = v["colorName"]
            image_list_message = v["images"]
            image_list = image_list_get(image_list_message)
            stock = '25'
            if sku_message["sizes"][size]["sizeCode"] not in v["sizes"]:
                stock = '0'
            sku = sku_handler(color,size,price,original_price,stock,image_list)
            specs.append(sku)
    image_url_list = specs[0]["images"]
    primary_image = image_url_list[0]
    for k,v in sku_message["colors"].items():
        primary_image = v["images"]["slot-1"]["zoom"]
    item["original_price"] = original_price
    item["primary_image"] = primary_image
    item["title"] = title
    item["url"] = url
    item["category1"] = Category
    item["price"] = price
    item["brand"] = brand
    item["images"] = image_url_list
    item["desc"] = desc


    result_dict = json.dumps({"items":item,"specs":specs})
    # result_dict = {"items":item,"specs":specs}
    # pprint.pprint(result_dict)
    return result_dict

if __name__ == "__main__":
    getInfo("http://cn.shopbop.com/gladiator-sandal-stuart-weitzman/vp/v=1/1548663033.htm?folderID=2534374302025763&fm=other-shopbysize&os=false&colorId=11781")






