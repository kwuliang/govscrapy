import time
from settings import *
from utils import *

def is_page_exist(resp):
    infos = parse_page(resp, "//h1/text()")
    if "404 Not Found" in infos:
        return False
    return True
def get_page(url):
    source_page = get_response(url)
    if not is_page_exist(source_page):
        return False
    infos = parse_page(source_page, "//td[@class='ewb-trade-td']/a/@href")
    for info in infos:
        detail_url = "http://jsggzy.jszwfw.gov.cn" + info
        
        resp = get_response(detail_url)
        filename = make_file_name(detail_url, "html")
        download_item(DATA_DIR,resp,filename)
    return True
   
for i in range(5):
    offset = f"00800{i}"
   # url = f"hltp://jsggzy.jszwfw.gov.cn/zcfg/{offset}/lawInfo.html"
    if offset == "008000":
        url = "http://jsggzy.jszwfw.gov.cn/zcfg/lawInfo.html"
        get_page(url)
        for i in range(50):
             sub_url = f"http://jsggzy.jszwfw.gov.cn/zcfg/{i}.html"  
             if not get_page(sub_url):
                 break

    elif offset == "008005":
        url = f"http://jsggzy.jszwfw.gov.cn/zcfg/{offset}/lawInfo2.html"
        get_page(url)
        for i in range(1,14):
            offset = f"00800500{i}"
            sub_url = f"http://jsggzy.jszwfw.gov.cn/zcfg/008005/{offset}/lawInfo2.html"
            get_page(url)
            for i in range(50):
                sub_url = f"http://jsggzy.jszwfw.gov.cn/zcfg/{i}.html"  
                if not get_page(sub_url):
                   break



    else:
        url = f"http://jsggzy.jszwfw.gov.cn/zcfg/{offset}/lawInfo2.html"
        get_page(url)
        for i in range(50):
            sub_url = f"http://jsggzy.jszwfw.gov.cn/zcfg/{i}.html"  
            if not get_page(sub_url):
               break

        

    




