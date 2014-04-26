from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem

class KupimeSpider(BaseSpider):
    name = "mojkupon"
    allowed_domains = ["mojkupon.hr"]
    start_urls = [
      "http://mojkupon.hr/deal/all/category/6",
	  "http://mojkupon.hr/deal/all/category/5",
	  "http://mojkupon.hr/deal/all/category/7"
    
     
    ]
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        #sites = hxs.select('//h1')
        links=hxs.select('//div[@class="allDeal"]')
        #links=hxs.select('//li')
        
        #links2=hxs.select('//ul[@id="all_offers"]//li')
        
        
        #sites = hxs.select('//div[@id="yt-lockup-content"]')
       
        items2 = []
        for site in links:
            item = DmozItem()
            #item['title']=site.select("a/@href").extract()
           
           
            item['title'] = site.select("div[@class='name']/a/text()").extract()
           
            item['category'] = hxs.select('//ul[@id="yw3"]/li[@class="active"]/a/text()').extract()
            #item['category'] = hxs.select('//ul[@id="yw3"]/li/text()').extract()
            item['link'] = site.select('div[@class="name"]/a/@href').extract()
            item['desc'] = ""
            item['dataorg']=""
           
            item['src'] = site.select("div[@class='image']/a/img/@src").extract()
           
           
            item['cijena'] = site.select("div/span/text()").extract()
           
           
           
            items2.append(item)
           
        return items2
   
