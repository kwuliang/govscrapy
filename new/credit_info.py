from utils import *
from settings import *

url = "http://jsggzy.jszwfw.gov.cn/xyxx/creditInfo.html"

for i in range(1,22):
    if i >= 2:
        url = f"http://jsggzy.jszwfw.gov.cn/xyxx/{i}.html"

    source_page = get_response(url)
    infos = parse_page(source_page, "//td[@class='ewb-trade-td']/a/@href")
   # print(infos)
    for info in infos:
        detail_url = "http://jsggzy.jszwfw.gov.cn" + info
        resp = get_response(detail_url)
        filename = make_file_name(detail_url, "html")
        download_item(DATA_DIR,resp,filename)
    

