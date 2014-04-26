from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem

class popustiplusSpider(BaseSpider):
    name = "popustplus"
    allowed_domains = ["popustplus.hr"]
    start_urls = [
    "https://www.popustplus.hr/component/enmasse/deal/display.html?locationId=&categoryId=1",
    "https://www.popustplus.hr/component/enmasse/deal/display.html?locationId=&categoryId=2",
    "https://www.popustplus.hr/component/enmasse/deal/display.html?locationId=&categoryId=3",
    "https://www.popustplus.hr/component/enmasse/deal/display.html?locationId=&categoryId=11",
    "https://www.popustplus.hr/component/enmasse/deal/display.html?locationId=&categoryId=4",
    "https://www.popustplus.hr/component/enmasse/deal/display.html?locationId=&categoryId=5",
    "https://www.popustplus.hr/component/enmasse/deal/display.html?locationId=&categoryId=6",
    "https://www.popustplus.hr/component/enmasse/deal/display.html?locationId=&categoryId=8",
    "https://www.popustplus.hr/component/enmasse/deal/display.html?locationId=&categoryId=10"
    
    
    ]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        #sites = hxs.select('//h1')
        links=hxs.select('//div[@class="maliDealContainer"]')
        #links=hxs.select('//li[@class="deal clearfix"]')
        
        
        #sites = hxs.select('//div[@id="yt-lockup-content"]')
        
        
        items2 = []
        for site in links:
            item = DmozItem()
            item['title'] = site.select('div[@class="maliDealInner"]/div[@class="malidealNaslov"]/a/text()').extract()
            item['category'] = response.url
            item['link'] = site.select('div[@class="maliDealInner"]/div[@class="malidealNaslov"]/a/@href').extract()
            item['desc'] = site.select('div[@class="deal-info"]/h3/text()').extract()
            item['dataorg']=""
            item['src'] = site.select('div[@class="maliDealInner"]/div[@class="maliDealSlika"]/a/img/@src').extract()
			
            item['cijena'] = site.select('div[@class="maliDealBottom"]/span/text()').extract()
            item['popust'] = ""
            
            
            items2.append(item)
        
        return items2
    
