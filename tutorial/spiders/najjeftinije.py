from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem

class KupimeSpider(BaseSpider):
    name = "najjeftinije"
    allowed_domains = ["najjeftinije.hr"]
    start_urls = [
      "http://najjeftinije.hr/offers/all/12/Autopraonice.html","http://najjeftinije.hr/offers/all/5/Frizerski-saloni.html"
    
     
    ]
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        #sites = hxs.select('//h1')
        #links=hxs.select('//div[@id="ndxmain_offer"]')
        #links=hxs.select('//li')
        
        links2=hxs.select('//ul[@id="all_offers"]//li')
        
        
        #sites = hxs.select('//div[@id="yt-lockup-content"]')
       
        items2 = []
        for site in links2:
            item = DmozItem()
            #item['title']=site.select("a/@href").extract()
           
           
            item['title'] = site.select("h3/a/text()").extract()
           
            item['category'] = hxs.select('//h1[@class="title"]/text()').extract()
			
            item['link'] = site.select("h3//a/@href").extract()
            item['desc'] = ""
            item['dataorg']=""
           
            item['src'] = site.select("a/@style").extract()
           
           
            item['cijena'] = site.select("h2/text()").extract()
           
           
           
            items2.append(item)
           
        return items2
   
