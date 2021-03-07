
import hashlib
import os
from scrapy.spiders.crawl import Rule, CrawlSpider
from scrapy.spiders.crawl import LinkExtractor
from govscrapy.items import MyspiderItem
from govscrapy.items import dataItem
from govscrapy.settings import DATA_DIR
from govscrapy.settings import WEBSITE
from govscrapy.settings import A_PATH
from govscrapy.settings import B_PATH
from govscrapy.settings import G_PATH
from govscrapy.settings import T_PATH
from govscrapy.utils import getStartUrls,Encode
from redis import Redis
from govscrapy.utils import get_extensions

count = 0
class cninSpider(CrawlSpider):
    name = 'cnin'

    websitePath = WEBSITE  #初始url存储路径

    # allowed_domains = ['www.cninfo.com.cn']
    # start_urls = ['http://www.cninfo.com.cn/new/index']
    # allowed_domains = ['chenhuafan.github.io']
    # start_urls = ['https://chenhuafan.github.io/blog']

    allowed_domains = ['www.cninfo.com.cn']
    start_urls = ['http://www.cninfo.com.cn/new/index']

    # allowed_domains, start_urls = getStartUrls(websitePath)

    # 连接redis
    conn = Redis(host='127.0.0.1', encoding='utf-8', port=6379)
    # print(conn)

    # allow=() is used to match all links
    rules = (
             Rule(LinkExtractor(), callback='parse',follow=True),
    )


#解析页面


    def parse(self, response):

        # 判断增量

        url = response.url
        key = Encode(url)
        ex = self.conn.sadd('keys', key)

        if ex == 1:
            print(url, " 数据有更新,爬取")
            # item = MyspiderItem(
            #     urldomain=None,
            #     html=None,
            #     pdf=[],
            #     xls=[],
            #     images=[],
            #     others=[]
            # )
            item = dataItem(
                urldomain=[],
                html=[],
                files=[]
            )
            abpath = DATA_DIR
            # 1.保存html
            filename = Encode(response.url) + ".html"

            item['html'] = filename

            domainUrl = response.url.split('/')[2]
            item['urldomain'] = Encode(domainUrl)
            abpath = abpath + item['urldomain']

            if not os.path.exists(abpath):  # 第一次创建文件夹

                os.makedirs(abpath)

            with open(abpath + '/' + filename, 'wb') as f:
                f.write(response.body)

            # 2.保存其他资源
            images = response.selector.xpath("//img/@src").extract()
            pdf = response.selector.xpath("//embed/@href[contains(.,'.pdf')]").extract() + response.selector.xpath("//embed/@href[contains(.,'.PDF')]").extract()
            xls = response.selector.xpath("//a/@href[contains(.,'.xls')]").extract() + response.selector.xpath("//a/@href[contains(.,'.XLS')]").extract()
            xlsx= response.selector.xpath("//a/@href[contains(.,'.xlsx')]").extract() + response.selector.xpath("//a/@href[contains(.,'.XLSX')]").extract()
            doc = response.selector.xpath("//a/@href[contains(.,'.doc')]").extract() + response.selector.xpath("//a/@href[contains(.,'.DOC')]").extract()
            docx = response.selector.xpath("//a/@href[contains(.,'.docx')]").extract() + response.selector.xpath("//a/@href[contains(.,'.DOCX')]").extract()
            # urls = images + pdf + xls
            # ahref = response.selector.xpath("//@href").extract()

            # ahref = self.link_extractor.extract_links(response.body)
            #
            urls =  images + pdf + xls + xlsx + docx + doc
            # file_url = response.selector.xpath("//a/@href]").extract()
            # urls = images + file_url
            if urls:
                for url in urls:
                    yield response.follow(url, callback=self.save_files, cb_kwargs=dict(item=item))
                    # if url.endswith('.html') or url.startwith('javascript'):
                    #     pass
                    # if url.startwith('javascript'):
                    #     pass
                    # else:
                    #     self.logger.info(url)
                    #     yield response.follow(url, callback=self.save_files, cb_kwargs=dict(item=item))


        else:
            print(url, " 数据没有进行更新")


    def save_files(self,response,item):

        abpath = DATA_DIR + item['urldomain']
        # response.Metadata
        # extens = get_extensions(response.body)
        # print('\n-------------,',extens)

        extens = get_extensions(response.url)


        filename = Encode(response.url) + extens

        with open(abpath +'/'+ filename, 'wb') as f:
            f.write(response.body)
            self.logger.info("Files downloading..." +filename)

        item["files"].append(filename)
        # if filename.endswith(".pdf"):
        #     item["pdf"].append(filename)
        # elif filename.endswith(".xls") or filename.endswith(".xlsx"):
        #     item["xls"].append(filename)
        # elif filename.endswith("png") or filename.endswith("jpg"):
        #     item["images"].append(filename)
        # else:
        #     item["others"].append(filename)


        return item








