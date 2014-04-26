from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem

class Kupizdravo(BaseSpider):
    name = "kupizdravo"
    allowed_domains = ["kupizdravo.hr"]
    start_urls = [
      "http://www.kupizdravo.hr/prijatelji-zdravlja/",
	  "http://www.kupizdravo.hr/zdravlje/",
	  "http://www.kupizdravo.hr/turizam/"
    
     
    ]
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        #sites = hxs.select('//h1')
        #links=hxs.select('//div[@class="item-content cf"]')
        links2=hxs.select('//li[@class="active-item"]')
        
        #links2=hxs.select('//ul[@id="all_offers"]//li')
        
        
        #sites = hxs.select('//div[@id="yt-lockup-content"]')
       
        items2 = []
        for site in links2:
            item = DmozItem()
            #item['title']=site.select("a/@href").extract()
           
            
            item['title'] = site.select('div[@class="item-content cf"]/div[@class="item-active"]/div[@class="item-text-active"]/p/a/text()').extract()
            
            #
            
            #site.select('div[@class="item-content cf"]').extract()
            #/div[@class="item-text-active"]/p/a/div[@class="item-active"]/text()
           
            #item['category'] = hxs.select('//ul[@id="yw3"]/li[@class="active"]/a/text()').extract()
            item['category'] = hxs.select('//title/text()').extract()
            item['link'] = site.select('div[@class="item-content cf"]/div[@class="item-right-active"]/a/@href').extract()
            item['desc'] = ""
            item['dataorg']=site.select('div[@class="item-content cf"]/div[@class="item-active"]/ul/li/span/text()').extract()
           
            item['src'] = site.select('div[@class="item-content cf"]/div[@class="item-right-active"]/a/img/@src').extract()
           
           
            item['cijena'] = site.select('div[@class="item-content cf"]/div[@class="item-active"]/ul/li/span[@class="recent-price"]/text()').extract()
           
            
           
            items2.append(item)
           
        return items2
   
