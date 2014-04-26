from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem
import os
#os.remove("/home/ivabla2/svipopusti/tutorial/items.json")

class DmozSpider(BaseSpider):
   name = "dmoz"
   allowed_domains = ["ponudadana.hr"]
   start_urls = [
       "http://www.ponudadana.hr/putovanja",
        "http://www.ponudadana.hr/zdravlje",
       "http://www.ponudadana.hr/hrana-i-pice",
       "http://www.ponudadana.hr/auti",
       "http://www.ponudadana.hr/edukacije",
       "http://www.ponudadana.hr/zabava",
       "http://www.ponudadana.hr/rekreacija"
      
   ]

   def parse(self, response):
       
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//h1')
       links=hxs.select('//div[@class="pp-title"]')
       links2=hxs.select('//div[@class="content-img"]')
       
       
       #scites = hxs.select('//div[@id="yt-lockup-content"]')
       
       
       items = []
       for site in links2:
           item = DmozItem()
           item['title'] = site.select("div[@class='pp-title']/a/h1/text()").extract()
           item['category'] = hxs.select('//title/text()').extract()
           item['link'] = site.select('a/@href').extract()
           item['desc'] = site.select("div[@class='pp-title']/a/h2/text()").extract()
           item['dataorg']=site.select('a/img/@data-original').extract()
           item['src'] = site.select('a/img/@src').extract()
           item['cijena'] = site.select("div[@class='pp-buy']/div[@class='buy-price']/text()").extract()
           
           
           
           items.append(item)
           
       
       print items    
       return items
       
