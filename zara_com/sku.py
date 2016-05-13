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



d ={"product":
    
        {"id":3230603,"type":"Product","kind":"Wear","sequence":0,
         "image":{"name":"3461001800_2_1","path":"/2016/V/0/1/p/3461/001/800/2/","timestamp":"1461239381438"},
         "xmedia":[{"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_1_1","width":1920,"height":2379,"timestamp":"1461239381438"},
                   {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_3_1","width":1920,"height":2379,"timestamp":"1461239395266"},
                   {"datatype":"xmedia","set":2,"type":"image","kind":"colorcut","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_3_1_1","width":1920,"height":2379,"timestamp":"1453743166999"},
                   {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_4_1","width":1920,"height":2379,"timestamp":"1461239403324"},
                   {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_5_1","width":1920,"height":2379,"timestamp":"1461239410166"},
                   {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_6_1","width":1920,"height":2379,"timestamp":"1461239418556"},
                   {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_2_1","width":1920,"height":2379,"timestamp":"1461239388411"},
                   {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_7_1","width":1920,"height":2379,"timestamp":"1461239426047"},
                   {"datatype":"xmedia","set":2,"type":"image","kind":"full","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_1_1_1","width":1920,"height":2379,"timestamp":"1461239434114"},
                   {"datatype":"xmedia","set":2,"type":"image","kind":"plain","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_6_1_1","width":1920,"height":2379,"timestamp":"1453743154113"}],
         "name":"LEATHER BIKER JACKET",
         "description":"Short leather jacket. Front lapels. Front pockets.HEIGHT OF MODEL: 176 CM. Size S",
         "isBuyable":'true',
         "price":19900,
         "tags":[],
         "detail":{"description":"Short leather jacket. Front lapels. Front pockets.HEIGHT OF MODEL: 176 CM. Size S",
                   "rawDescription":"Short leather jacket. Front lapels. Front pockets.\u003cbr/>\u003cbr/>HEIGHT OF MODEL: 176 CM. Size S",
                   "reference":"03461001-V2016",
                   "displayReference":"3461/001",
                   "composition":[],
                   "care":[{"id":"7000000000000003501","name":"9","description":"DO NOT WASH"},
                           {"id":"7000000000000003502","name":"14","description":"DO NOT BLEACH"},
                           {"id":"7000000000000003503","name":"19","description":"DO NOT IRON"},
                           {"id":"7000000000000003504","name":"28","description":"DO NOT DRY CLEAN"},
                           {"id":"7000000000000003505","name":"35","description":"DO NOT TUMBLE DRY"}],
                   "colors":[{"id":"800",
                              "name":"Black",
                              "image":{"name":"3461001800_2_1","path":"/2016/V/0/1/p/3461/001/800/2/","timestamp":"1461239381438"},
                              "colorImageUrl":"http://static.zara.net/photos//2016/V/0/1/p/3461/001/800/2//w/135/3461001800_3_1.jpg?timestamp=1453743166999",
                              "colorImage":{"name":"3461001800_3_1","path":"/2016/V/0/1/p/3461/001/800/2/","timestamp":"1453743166999"},
                              "detailImages":[{"name":"3461001800_2_3","path":"/2016/V/0/1/p/3461/001/800/2/","timestamp":"1461239395266"},
                                              {"name":"3461001800_2_4","path":"/2016/V/0/1/p/3461/001/800/2/","timestamp":"1461239403324"},
                                              {"name":"3461001800_2_5","path":"/2016/V/0/1/p/3461/001/800/2/","timestamp":"1461239410166"},
                                              {"name":"3461001800_2_6","path":"/2016/V/0/1/p/3461/001/800/2/","timestamp":"1461239418556"},
                                              {"name":"3461001800_2_2","path":"/2016/V/0/1/p/3461/001/800/2/","timestamp":"1461239388411"},
                                              {"name":"3461001800_2_7","path":"/2016/V/0/1/p/3461/001/800/2/","timestamp":"1461239426047"},
                                              {"name":"3461001800_1_1","path":"/2016/V/0/1/p/3461/001/800/2/","timestamp":"1461239434114"},
                                              {"name":"3461001800_6_1","path":"/2016/V/0/1/p/3461/001/800/2/","timestamp":"1453743154113"}],

                              "detailFlatImages":[],
                              "sizeGuideImages":[],
                              "videos":[],
                              "xmedia":[{"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_1_1","width":1920,"height":2379,"timestamp":"1461239381438","order":1},
                                        {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_3_1","width":1920,"height":2379,"timestamp":"1461239395266","order":2},
                                        {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_4_1","width":1920,"height":2379,"timestamp":"1461239403324","order":3},
                                        {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_5_1","width":1920,"height":2379,"timestamp":"1461239410166","order":4},
                                        {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_6_1","width":1920,"height":2379,"timestamp":"1461239418556","order":5},
                                        {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_2_1","width":1920,"height":2379,"timestamp":"1461239388411","order":6},
                                        {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_7_1","width":1920,"height":2379,"timestamp":"1461239426047","order":7},
                                        {"datatype":"xmedia","set":2,"type":"image","kind":"plain","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_6_1_1","width":1920,"height":2379,"timestamp":"1453743154113","order":8}],
                              "sizes":[{"sku":3231427,"id":1,"name":"XS","price":19900,"availability":"in_stock"},
                                       {"sku":3231426,"id":2,"name":"S","price":19900,"availability":"in_stock"},
                                       {"sku":3231431,"id":3,"name":"M","price":19900,"availability":"in_stock"},
                                       {"sku":3231429,"id":4,"name":"L","price":19900,"availability":"in_stock"},
                                       {"sku":3231432,"id":5,"name":"XL","price":19900,"availability":"out_of_stock"}],
                              "isStockClearance":'false',
                              "colorCutImg":{"datatype":"xmedia","set":2,"type":"image","kind":"colorcut","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_3_1_1","width":1920,"height":2379,"timestamp":"1453743166999"},
                              "modelImgs":[{"datatype":"xmedia","set":2,"type":"image","kind":"plain","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_6_1_1","width":1920,"height":2379,"timestamp":"1453743154113","order":8}],
                              "mainImgs":[{"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_1_1","width":1920,"height":2379,"timestamp":"1461239381438","order":1},
                                          {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_3_1","width":1920,"height":2379,"timestamp":"1461239395266","order":2},
                                          {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_4_1","width":1920,"height":2379,"timestamp":"1461239403324","order":3},
                                          {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_5_1","width":1920,"height":2379,"timestamp":"1461239410166","order":4}],
                              "detailImgs":[{"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_6_1","width":1920,"height":2379,"timestamp":"1461239418556","order":5},
                                            {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_2_1","width":1920,"height":2379,"timestamp":"1461239388411","order":6},
                                            {"datatype":"xmedia","set":2,"type":"image","kind":"other","path":"/2016/V/0/1/p/3461/001/800/2","name":"3461001800_2_7_1","width":1920,"height":2379,"timestamp":"1461239426047","order":7}]}],
                   "relatedProducts":[{"id":3509012,"type":"Product","kind":"Wear","sequence":0,"reference":"02728435-V2016","image":{"name":"2728435403_6_1","path":"/2016/V/0/1/p/2728/435/403/2/","timestamp":"1459788065303"},"xmedia":[{"datatype":"xmedia","set":2,"type":"image","kind":"plain","path":"/2016/V/0/1/p/2728/435/403/2","name":"2728435403_6_1_1","width":1920,"height":2379,"timestamp":"1459788065303"}],"categoryId":358031,"name":"LONG POPLIN DRESS","isBuyable":'true',"price":6990,"bundleProductSummaries":[],"tags":[],"section":0,"extraInfo":{},"seo":{"title":"LONG POPLIN DRESS-View All-OUTERWEAR-WOMAN | ZARA United States","metaDescription":"LONG POPLIN DRESS","mainHeader":"LONG POPLIN DRESS","description":"Long dress. Long sleeves. Round neck. Lapel collar. Flounce skirt.\u003cbr/br>\u003cbr/br>HEIGHT OF MODEL 175 cm.","bannerPosition":0,"breadCrumb":[{"text":"WOMAN","keyword":"woman","id":358501},{"text":"OUTERWEAR","keyword":"woman/outerwear","id":367501},{"text":"View All","keyword":"woman/outerwear/view-all","id":719012},{"text":"LONG POPLIN DRESS","id":0}]},"tagTypes":[]}],"bundleProducts":[],"detailedComposition":{"parts":[{"description":"OUTER SHELL","areas":[],"components":[{"material":"sheep leather","percentage":"100%"}],"microcontents":[],"reinforcements":[]},{"description":"LINING","areas":[{"description":"BODY LINING","components":[{"material":"polyester","percentage":"100%"}]},{"description":"SLEEVE LINING","components":[{"material":"polyester","percentage":"100%"}]}],"components":[],"microcontents":[],"reinforcements":[]}],"exceptions":[]},"categories":[],"isBuyable":'true',"layout":{"type":"DFLT_PRODUCT_VW","attr":{}}},"section":1,"extraInfo":{"isSizeLabelExplanationRequired":'false'},"seo":{"keyword":"woman/outerwear/view-all/leather-biker-jacket","canonical":"http://www.zara.com/us/en/woman/leather/real-leather/leather-biker-jacket-c813524p3233177.html","title":"LEATHER BIKER JACKET-View All-OUTERWEAR-WOMAN | ZARA United States","metaDescription":"LEATHER BIKER JACKET","mainHeader":"LEATHER BIKER JACKET","description":"Short leather jacket. Front lapels. Front pockets.\u003cbr/>\u003cbr/>HEIGHT OF MODEL: 176 CM. Size S","bannerPosition":0,"breadCrumb":[{"text":"WOMAN","keyword":"woman","id":358501,"seo":{"keyword":"woman"}},{"text":"OUTERWEAR","keyword":"woman/outerwear","id":367501,"seo":{"keyword":"woman/outerwear"}},{"text":"View All","keyword":"woman/outerwear/view-all","id":719012,"seo":{"keyword":"woman/outerwear/view-all"}},{"text":"LEATHER BIKER JACKET","id":0}]},"tagTypes":[],"referenceType":"0"},"parentId":"3233177","category":{"id":719012,"key":"V2016-MUJER-ABRIGOS-VER_TODOS","name":"View All","layoutWeb":"products-category-view","layoutApp":"list","type":"45","viewCategoryId":0,"subcategories":[],"seo":{"keyword":"woman/outerwear/view-all","title":"Summer Coats for Women | ZARA United States","metaDescription":"Latest Spring/Summer trends for women's coats at ZARA online. Find long, short, peacoats, trench, military, fur, faux fur and leather coats and vests for women.","metaKeywords":"Trench coat, peacoat, coats, faux fur vest, fur vest, pea coat, raincoat, faux fur coat, fur coats, ","mainHeader":"OUTERWEAR FOR WOMEN","description":"Long, short, peacoats, trench, military, fur, faux fur and leather coats and vests for women.","bannerPosition":-1,"breadCrumb":[{"text":"WOMAN","keyword":"woman","id":358501},{"text":"OUTERWEAR","keyword":"woman/outerwear","id":367501},{"text":"View All","keyword":"woman/outerwear/view-all","id":719012}]},"layoutWebMobile":"products-category-view","published":["app","store","web","web-mobile"],"attributeList":[{"key":"REVERSE_IDENTITY","value":"SODOT_REV-SOGIRBA-REJUM-6102V"},{"key":"TIME-LINE","value":"TIME-LINE"}],"isStockClearance":'false'},"docInfo":{"bodyId":"catalog-area","bodyClass":"product-detail-page product-page","lastModified":"2016-05-12@04:43:06 +01:00","title":"LEATHER BIKER JACKET - View All-OUTERWEAR-WOMAN | ZARA United States","description":"LEATHER BIKER JACKET","pageId":"product-3230603","seoAttributes":"itemscope itemtype=\"http://schema.org/WebPage\"","relData":{"canonicalUrl":"http://www.zara.com/us/en/woman/leather/real-leather/leather-biker-jacket-c813524p3233177.html","alternateMobile":{"href":"http://m.zara.com/us/en/woman/outerwear/view-all/leather-biker-jacket-c719012p3230603.html"}}},"breadCrumbs":[{"text":"WOMAN","keyword":"woman","id":358501,"seo":{"keyword":"woman"}},{"text":"OUTERWEAR","keyword":"woman/outerwear","id":367501,"seo":{"keyword":"woman/outerwear"}},{"text":"View All","keyword":"woman/outerwear/view-all","id":719012,"seo":{"keyword":"woman/outerwear/view-all"}},{"text":"LEATHER BIKER JACKET","id":0}],"analyticsData":{"appVersion":"1.8.0-b.25","pageType":"PRODUCT_DETAILS","page":{"language":"en","shop":"US"},"trackerUA":"UA-18083935-1","anonymizeIp":"0","hostname":"web-pc.zara.com","catGroupId":719012,"catIdentifier":"V2016-MUJER-ABRIGOS-VER_TODOS","productRef":"03461001-V2016"},"mobileApp":{"msg":"Do you want to open this product in Zara app?","iOSUri":"zara:///1/products?partNumber=03461001800","androidUri":"intent:///1/products?partNumber=03461001800#Intent;scheme=zara;package=com.inditex.zara;end"},"isSharedProduct":'false',"isContactEnabled":'true',"viewName":"catalog/product-detail","renderingContext":"server"}

pprint.pprint(d)