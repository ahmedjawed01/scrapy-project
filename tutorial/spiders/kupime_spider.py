from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tutorial.items import DmozItem

class KupimeSpider(BaseSpider):
   name = "kupime"
   allowed_domains = ["kupime.hr"]
   start_urls = [
       "http://www.kupime.hr/grad/zagreb/putovanja/",
	   "http://www.kupime.hr/grad/zagreb/hrana-i-pice/",
	   "http://www.kupime.hr/grad/zagreb/ljepota/",
	   "http://www.kupime.hr/grad/zagreb/cuvari-zdravlja/",
	   "http://www.kupime.hr/grad/zagreb/sport-i-rekreacija/"
     
      
   ]

   def parse(self, response):
       hxs = HtmlXPathSelector(response)
       #sites = hxs.select('//h1')
       links=hxs.select('//div[@id="ndxmain_offer"]')
       #links=hxs.select('//li')
       
       #links2=hxs.select('//li[@class="cf"]')
       
       
       #sites = hxs.select('//div[@id="yt-lockup-content"]')
       
       
       items2 = []
       for site in links:
           item = DmozItem()
           #item['title']=site.select("a/@href").extract()
           
           
           item['title'] = site.select("div[@id='ndxoffer_title']/a/strong/text()").extract()
		   
           item['category'] = hxs.select('//title/text()').extract()
           item['link'] = site.select("div[@id='ndxoffer_title']/a/@href").extract()
           item['desc'] = site.select("div[@id='ndxoffer_title']/a/span/text()").extract()
           item['dataorg']=""
		   
           item['src'] = site.select("div[@id='ndxoffer_tech']/div[@id='ndxmain_img']/a/img/@src").extract()
           
           
           item['cijena'] = site.select("div[@id='ndxoffer_tech']/div[@id='ndxspecs']/div[@id='ndxprice_box']/div[@id='ndxprice']/text()").extract()
           
           
           
           items2.append(item)
           
       return items2
       
