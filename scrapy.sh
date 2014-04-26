#!/bin/sh

cd /home/ivabla2/svipopusti/tutorial

PATH=$PATH:/usr/local/bin
export PATH

/home/ivabla2/lib/python2.7/site-packages/Scrapy-0.21.0-py2.7.egg/EGG-INFO/scripts/scrapy crawl dmoz -o items.json -t json  
/home/ivabla2/lib/python2.7/site-packages/Scrapy-0.21.0-py2.7.egg/EGG-INFO/scripts/scrapy crawl crnojaje -o items1.json -t json   
/home/ivabla2/lib/python2.7/site-packages/Scrapy-0.21.0-py2.7.egg/EGG-INFO/scripts/scrapy crawl kolektiva -o items2.json -t json  
/home/ivabla2/lib/python2.7/site-packages/Scrapy-0.21.0-py2.7.egg/EGG-INFO/scripts/scrapy crawl kupime -o items3.json -t json   
/home/ivabla2/lib/python2.7/site-packages/Scrapy-0.21.0-py2.7.egg/EGG-INFO/scripts/scrapy crawl kupisve -o items4.json -t json  
/home/ivabla2/lib/python2.7/site-packages/Scrapy-0.21.0-py2.7.egg/EGG-INFO/scripts/scrapy crawl kupizdravo -o items5.json -t json   
/home/ivabla2/lib/python2.7/site-packages/Scrapy-0.21.0-py2.7.egg/EGG-INFO/scripts/scrapy crawl megapopust -o items6.json -t json  
/home/ivabla2/lib/python2.7/site-packages/Scrapy-0.21.0-py2.7.egg/EGG-INFO/scripts/scrapy crawl mojkupon -o items7.json -t json 
/home/ivabla2/lib/python2.7/site-packages/Scrapy-0.21.0-py2.7.egg/EGG-INFO/scripts/scrapy crawl najjeftinije -o items8.json -t json   
/home/ivabla2/lib/python2.7/site-packages/Scrapy-0.21.0-py2.7.egg/EGG-INFO/scripts/scrapy crawl popustplus -o items9.json -t json  
/home/ivabla2/lib/python2.7/site-packages/Scrapy-0.21.0-py2.7.egg/EGG-INFO/scripts/scrapy crawl promotiva -o items10.json -t json  
/home/ivabla2/bin/python /home/ivabla2/svipopusti/tutorial/mongodb.py >> /home/ivabla2/svipopusti/tutorial/mongo.log 




