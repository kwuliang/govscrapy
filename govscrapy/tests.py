
# url = 'http://www.chinafx.gov.cn/default.htm'
#
# res = url.split("/")
# print(res[2])
# # lis = url.find('/')
# # print(lis)
#
# # lisa = url.index('/',7)
# # print(lisa)
#
# # print(url[0:lisa])
import pymongo


def getStartUrls(path):
    allowed_domains = []
    start_urls = []
    webnames=[]
    with open(path, 'r', encoding='utf-8') as infos:
        for info in infos:
            # print(info)
            arrs = info.split('\t',1)
            webnames.append(arrs[0])
            start_urls.append(arrs[-1].replace("\n", ""))
            allowed_domains.append(arrs[-1].split('/')[2])

    return webnames, allowed_domains, start_urls

# websitePath='D:/Aworkspace/scrapydata/website.txt'

# names,allowed_domains, start_urls = getStartUrls(websitePath)
#
# print(names)


def getDomain(strUrl):
    res = strUrl.split("/")[2]
    print(res)
#
# url = 'http://www.chinafx.gov.cn:90/default.htm'
#
# getDomain(url)

import redis
def redistest():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    # r.hvals('keys')
    r.delete('keys')

    # print(r.get('foo'))
    print('redis 已清空')

def mongodb():
    client = pymongo.MongoClient('127.0.0.1:27017')
    db = client['scrapy_gov']
    table = db['scrapy_gov_items']
    x = table.delete_many({})

    print(x.deleted_count, "个文档已删除...mongodb已清空")

redistest()
mongodb()
from govscrapy.utils import get_extensions

# get_extensions('E:/data/test/website.txt')
# get_extensions('E:/data/test/website.xls')
# get_extensions('E:/data/test/1.doc')
# get_extensions('E:/data/test/1.jpg')
# get_extensions('E:/data/test/1.png')
# get_extensions('E:/data/test/1.pdf')