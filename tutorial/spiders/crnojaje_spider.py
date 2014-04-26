from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem

class CrnojajeSpider(BaseSpider):
   name = "crnojaje"
   allowed_domains = ["crnojaje.hr"]
   start_urls = [
       "http://www.crnojaje.hr/Deals/DealList/Putovanja",
       "http://www.crnojaje.hr/Deals/DealList/Zabava-i-sport",
       "http://www.crnojaje.hr/Deals/DealList/Zdravlje",
       "http://www.crnojaje.hr/Deals/DealList/Gastro"
      
   ]

   def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//h1')
       links=hxs.select('//div[@class="pp-title"]')
       links2=hxs.select('//li[@class="cf"]')
       
       
       #sites = hxs.select('//div[@id="yt-lockup-content"]')
       
       
       items2 = []
       for site in links2:
           item = DmozItem()
           item['title'] = site.select("a/h3/text()").extract()
           item['category'] = hxs.select('//title/text()').extract()
           item['link'] = site.select('a/@href').extract()
           item['desc'] = ""
           item['dataorg']=""
           item['src'] = site.select('a/img/@src').extract()
           item['cijena'] = site.select("a/div[@class='cijene']/div[@class='column cijena']/strong/text()").extract()
           
           
		   
           items2.append(item)
           
       return items2
       
