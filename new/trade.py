import json
import time
from utils import *
from settings import *


def get_urls(page_offset):
    base_url = 'http://jsggzy.jszwfw.gov.cn/inteligentsearch/rest/inteligentSearch/getFullTextData'
    data = '{"token":"","pn":'+str(page_offset * 2) + ',"rn":20,"sdt":"","edt":"","wd":null,"inc_wd":"","exc_wd":"","fields":"title","cnum":"001","sort":"{\\"infodatepx\\":\\"0\\"}","ssort":"title","cl":200,"terminal":"","condition":[],"time":[{"fieldName":"infodatepx","startTime":"2021-03-06 00:00:00","endTime":"2021-03-09 23:59:59"}],"highlights":"title","statistics":null,"unionCondition":null,"accuracy":"","noParticiple":"1","searchRange":null,"isBusiness":"1"}'
    response = get_response(url=base_url, data=data)
    #print(response.text)
    resp_json = json.loads(response.text)
    records = resp_json["result"]["records"]
    records_list = []
    for record in records:
        records_list.append(
                    {
                        "ca":record["categorynum"],
                        "linkurl":record["linkurl"]
                    }
                    )
    return records_list

def parse_url(data_url):
    if data_url["ca"][0:6] == "003010":
        url = "http://jsggzy.jszwfw.gov.cn/ypcghtml" + data_url["linkurl"]
    else:
        url = "http://jsggzy.jszwfw.gov.cn" + data_url["linkurl"]
    return url


for i in range(50):
    urls_list = get_urls(i)
    for url_item in urls_list:
        url = parse_url(url_item)
        resp = get_response(url)
        filename = make_file_name(resp, "html")
        download_item(DATA_DIR, resp, filename)
        time.sleep(1)



