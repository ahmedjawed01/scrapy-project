from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem

class KolektivaSpider(BaseSpider):
    name = "kolektiva"
    allowed_domains = ["kolektiva.hr"]
    start_urls = [
    "http://www.kolektiva.hr/travel/",
    
    
    ]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        #sites = hxs.select('//h1')
        #links=hxs.select('//div[@class="deal-info"]')
        links=hxs.select('//li[@class="deal clearfix"]')
        
        
        #sites = hxs.select('//div[@id="yt-lockup-content"]')
        
        
        items2 = []
        for site in links:
            item = DmozItem()
            item['title'] = site.select('div[@class="deal-info"]/h2/a/text()').extract()
            item['category'] = hxs.select('//title/text()').extract()
            item['link'] = site.select('div[@class="deal-info"]/h2/a/@href').extract()
            item['desc'] = site.select('div[@class="deal-info"]/h3/text()').extract()
            item['dataorg']=""
            item['src'] = site.select('a/img/@src').extract()
			
            item['cijena'] = site.select('div[@class="deal-info"]/div[@class="values clearfix"]/div[@class="prices first"]/span[@class="price value"]/text()').extract()
            item['popust'] = site.select('div[@class="deal-info"]/div[@class="values clearfix"]/div[@class="prices discount"]/span[@class="price"]/text()').extract()
            
            
            items2.append(item)
        
        return items2
    
