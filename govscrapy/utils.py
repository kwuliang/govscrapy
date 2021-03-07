import xlrd
import hashlib
import  magic
import re

def getStartUrls(path):

    allowed_domains = []
    start_urls = []
    if path.endswith(".txt"):
        allowed_domains, start_urls = read_txt(path)
    elif path.endswith(".xls"):
        allowed_domains, start_urls = read_excel(path)
    else:
        print("站点格式请使用txt格式或者excel")

    return allowed_domains, start_urls

def read_txt(path):
    allowed_domains = []
    start_urls = []
    with open(path, 'r', encoding='utf-8') as infos:
        for info in infos:  # 跳过第一行
            # print(info)
            arrs = info.split('\t', 1)
            start_urls.append(arrs[-1].replace("\n", ""))
            allowed_domains.append(arrs[-1].split('/')[2])

    return allowed_domains, start_urls

def read_excel(path):
    allowed_domains = []
    start_urls = []

    workbook=xlrd.open_workbook(path)
    # 获取所有sheet
    # sheet_name = workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    sheet = workbook.sheet_by_index(0)  # sheet索引从0开始
    cols = sheet.col_values(1) # 获取第2列内容

    for info in cols:  # 跳过第一行
        # print(info)
        start_urls.append(info)
        allowed_domains.append(info.split('/')[2])

    return allowed_domains, start_urls



#test

# allowed_domains, start_urls  = getStartUrls('E:/data/scrapydata/website.xls')
#
# print(start_urls)

#使用时间戳来进行md5编码，减少重名可能性
def Encode(urlStr):
    # millis = str(time.time())
    m = hashlib.md5(urlStr.encode("utf-8"))
    res = m.hexdigest()
    return res

def get_extensions(url):
    extens = 'html'
    if  re.findall('.pdf', url, flags=re.IGNORECASE): #'.PDF' in url or '.pdf' in url:
        extens = '.pdf'
    elif  re.findall('.doc', url, flags=re.IGNORECASE): #'.doc' in url or '.DOC' in url:
        extens = '.doc'
    elif  re.findall('.docx', url, flags=re.IGNORECASE):#'.docx' in url or '.DOCC' in url:
        extens = '.docx'
    elif  re.findall('.xls', url, flags=re.IGNORECASE):#'.xls' in url or '.XLS' in url:
        extens = '.xls'
    elif re.findall('.xlsx', url, flags=re.IGNORECASE):#'.xlsx' in url or '.XLSX' in url:
        extens = '.xlsx'
    elif re.findall('.png', url, flags=re.IGNORECASE) :
        extens = '.png'
    elif re.findall('.jpg', url, flags=re.IGNORECASE):
        extens = '.jpg'

    return extens
    # return

print(get_extensions('sdfs.jpgsdfsd'))