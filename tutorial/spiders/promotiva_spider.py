from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem
import os
#os.remove("/home/ivabla2/svipopusti/tutorial/items.json")

class PromotivaSpider(BaseSpider):
   name = "promotiva"
   allowed_domains = ["promotiva.hr"]
   start_urls = [
       "http://www.promotiva.hr/promotiva-travel.html",
      
      
   ]

   def parse(self, response):
       
       hxs = HtmlXPathSelector(response)
       #sites = hxs.select('//h1')
       links=hxs.select('//div[@class="browseProductContainer"]')
       #links2=hxs.select('//div[@class="content-img"]')
       
       
       #scites = hxs.select('//div[@id="yt-lockup-content"]')
       
       
       items = []
       for site in links:
           item = DmozItem()
           item['title'] = site.select('table/tr/td/table/tr/td[@class="header3"]/a/center/text()').extract()
           item['category'] = hxs.select('//title/text()').extract()
           item['link'] = site.select('table/tr/td/table/tr/td[@class="header3"]/a/@href').extract()
           item['desc'] = ""
           item['dataorg']=""
           item['src'] = site.select('table/tr/td/img[@class="ponudaimage clearfix"]/@src').extract()
           
           item['cijena'] = site.select('table/tr/td/table/tr/td[@class="ponudacijena3"]/span[@class="productPrice"]/text()').extract()
           
           
           print items
           items.append(item)
           
       
           
       return items
       
