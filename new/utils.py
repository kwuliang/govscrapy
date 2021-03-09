import requests
import json
from lxml import etree
import hashlib

def get_response(url,**kwargs):
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "en-US,en;q=0.5", 
    "Dnt": "1", 
    "Sec-Gpc": "1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.107 Safari/537.36", 
  }
    if not kwargs:
        response = requests.get(url=url,headers=headers,verify=False)
    elif kwargs["data"]:
        data=kwargs["data"]
        response = requests.post(url=url,headers=headers,data=data,verify=False)
    else:
        return None
        
    return response


def download_item(DATA_DIR, resp, filename):
    if DATA_DIR.endswith("/"):
        loc = DATA_DIR + filename
    else:
        loc = DATA_DIR +"/"+ filename

    with open(loc, "wb") as f:
        print(f"[+] Downloading {filename} ...")
        f.write(resp.content)

def parse_page(resp, xpath_pattern):
    html = etree.HTML(resp.content)
    infos = html.xpath(xpath_pattern)

    return infos

def make_file_name(raw_name, extension):
    md5 = hashlib.md5()
    md5.update(str(raw_name).encode("utf-8"))
    return md5.hexdigest() + "." + extension
