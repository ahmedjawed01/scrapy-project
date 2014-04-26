from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem

class MegapopustSpider(BaseSpider):
   name = "megapopust"
   allowed_domains = ["megapopust.hr"]
   start_urls = [
       "http://megapopust.hr/putovanja",
	   "http://megapopust.hr/restorani",
	   "http://megapopust.hr/zdravlje-i-ljepota",
	   "http://megapopust.hr/sport-i-zabava",
	   "http://megapopust.hr/najam-vozila"
      
   ]

   def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//h1')
       links=hxs.select('//div[@class="offer wide clearfix"]')
       links2=hxs.select('//li[@class="cf"]')
       
       
       #sites = hxs.select('//div[@id="yt-lockup-content"]')
       
       
       items2 = []
       for site in links:
           item = DmozItem()
           item['title'] = site.select("div[@class='details']/h3/a/text()").extract()
		   
           item['category'] = hxs.select("//div[@class='main-title clearfix']/h2/text()").extract()
           item['link'] = site.select('div[@class="photo"]/a/@href').extract()
           item['desc'] = ""
           item['dataorg']=site.select("div[@class='details']/ul[@class='save clearfix']/li[@class='item-3']/text()").extract()
		   
           item['src'] = site.select('div[@class="photo"]/a/img/@src').extract()
           item['cijena'] = site.select("div[@class='details']/ul[@class='save clearfix']/li[@class='item-1']/span/text()").extract()
           
           
		   
           items2.append(item)
           
       return items2
       
