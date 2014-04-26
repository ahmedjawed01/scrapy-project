'''
Created on Nov 3, 2013

@author: blaz1988
'''
'''
Created on Nov 3, 2013

@author: blaz1988
'''
import pymongo
import json
from pymongo import MongoClient
from datetime import datetime
import random
import re



print "Pocetak izvrsavanja mogodb.py"
print datetime.now()
mongo = pymongo.Connection('127.0.0.1')
db = mongo['database']
json_ponuddana=open('/home/ivabla2/svipopusti/tutorial/items.json')
json_crnojaje=open('/home/ivabla2/svipopusti/tutorial/items1.json')
json_kupime=open('/home/ivabla2/svipopusti/tutorial/items3.json')
json_kolektiva=open('/home/ivabla2/svipopusti/tutorial/items2.json')
json_najjeftinije=open('/home/ivabla2/svipopusti/tutorial/items8.json')
json_kupisve=open('/home/ivabla2/svipopusti/tutorial/items4.json')
json_mojkupon=open('/home/ivabla2/svipopusti/tutorial/items7.json')
json_kupizdravo=open('/home/ivabla2/svipopusti/tutorial/items5.json')
json_megapopust=open('/home/ivabla2/svipopusti/tutorial/items6.json')
json_popustplus=open('/home/ivabla2/svipopusti/tutorial/items9.json')
json_promotiva=open('/home/ivabla2/svipopusti/tutorial/items10.json')



data_ponuddana = json.load(json_ponuddana)
data_crnojaje = json.load(json_crnojaje)
data_kupime = json.load(json_kupime)
data_kolektiva = json.load(json_kolektiva)
data_najjeftinije = json.load(json_najjeftinije)
data_kupisve = json.load(json_kupisve)
data_mojkupon = json.load(json_mojkupon)
data_kupizdravo = json.load(json_kupizdravo)
data_megapopust = json.load(json_megapopust)
data_popustplus = json.load(json_popustplus)
data_promotiva = json.load(json_promotiva)

i=0

for d in data_ponuddana:
    kategorija="Nista"
    if 'Zdravlje' in d['category'][0]:
        kategorija='Zdravlje'
    elif 'Putovanja' in d['category'][0]:
        kategorija='Putovanja'
    elif 'Hrana' in d['category'][0]:
        kategorija='Hrana'
    elif 'Auti' in d['category'][0]:
        kategorija='Auti'
    elif 'Edukacije' in d['category'][0]:
        kategorija='Edukacije'
    elif 'Zabava' in d['category'][0]:
        kategorija='Zabava'
    elif 'Rekreacija' in d['category'][0]:
        kategorija='Rekreacija'
    link=d['link'][0]
    link=link.strip()
    title=d['title'][0]
    title=title.strip()
    title=title.upper()
    img=d['src'][0]
    img=img.strip()
    if d['dataorg']:
        img=d['dataorg'][0]
        img=img.strip()
    desc=d['desc'][0]
    desc=desc.strip()
    cijena=d['cijena'][0]
    cijena=cijena.strip()
        
    i=i+1
    db.ponude.save(
   {
     '_id': link,
     'title': title,
     'link': link,
     'img': img,
     'desc': desc,
                     'likes':0,
                     'counter':i,
                     'datetime':datetime.now(),
                     'kategorija':kategorija,
                     'cijena':cijena,
     'Web_Stranica':"ponudadana.hr",
     'random':random.randint(1,100000)
     
   }
)
    
    


for d in data_crnojaje:
    kategorija="Nista"
    if 'Zdravlje' in d['category'][0]:
        kategorija='Zdravlje'
    elif 'Putovanja' in d['category'][0]:
        kategorija='Putovanja'
    elif 'Hrana' in d['category'][0] or 'Gastro' in d['category'][0]:
        kategorija='Hrana'
    elif 'Auti' in d['category'][0]:
        kategorija='Auti'
    elif 'Edukacije' in d['category'][0]:
        kategorija='Edukacije'
    elif 'Zabava' in d['category'][0]:
        kategorija='Zabava'
    elif 'Rekreacija' in d['category'][0]:
        kategorija='Rekreacija'
    link=d['link'][0]
    link=link.strip()
    link="http://www.crnojaje.hr"+link
    title=""
    for t in d['title']:
        title=title+t
    title=title.strip()
    title=title.upper()
    img=d['src'][0]
    img=img.strip()
    
    desc=d['desc']
    desc=desc.strip()
    cijena=d['cijena'][0]
    cijena=cijena.strip()
    cijena=cijena.split("kn")
    cijena=cijena[0]
        
    i=i+1
    db.ponude.save(
   {
     '_id': link,
     'title': title,
     'link': link,
     'img': img,
     'desc': desc,
                     'likes':0,
                     'counter':i,
                     'datetime':datetime.now(),
                     'kategorija':kategorija,
                     'cijena':cijena,
     'Web_Stranica':"crnojaje.hr",
     'random':random.randint(1,100000)
     
   }
)
        
        


for d in data_kupime:
    kategorija="Nista"
    if 'Zdravlje' in d['category'][0] or 'zdravlja' in d['category'][0]:
        kategorija='Zdravlje'
    elif 'Putovanja' in d['category'][0]:
        kategorija='Putovanja'
    elif 'Hrana' in d['category'][0] or 'Gastro' in d['category'][0]:
        kategorija='Hrana'
    elif 'Auti' in d['category'][0]:
        kategorija='Auti'
    elif 'Edukacije' in d['category'][0]:
        kategorija='Edukacije'
    elif 'Zabava' in d['category'][0]:
        kategorija='Zabava'
    elif 'Rekreacija' in d['category'][0] or 'rekreacija' in d['category'][0]:
        kategorija='Rekreacija'
    link=d['link'][0]
    link=link.strip()
    link="http://www.kupime.hr"+link
    title=""
    for t in d['title']:
        title=title+t
    title=title.strip()
    title=title.upper()
    img=d['src'][0]
    img=img.strip()
    img="http://www.kupime.hr"+img
    
    desc=d['desc'][0]
    desc=desc.strip()
    cijena=d['cijena'][0]
    cijena=cijena.strip()
        
    i=i+1
    db.ponude.save(
   {
     '_id': link,
     'title': title,
     'link': link,
     'img': img,
     'desc': desc,
                     'likes':0,
                     'counter':i,
                     'datetime':datetime.now(),
                     'kategorija':kategorija,
                     'cijena':cijena,
     'Web_Stranica':"kupime.hr",
     'random':random.randint(1,100000)
     
   }
)
    
for d in data_kolektiva:
    kategorija="Nista"
    if 'Zdravlje' in d['category'][0]  or 'zdravlja' in d['category'][0]:
        kategorija='Zdravlje'
    elif 'travel' in d['link'][0]:
        kategorija='Putovanja'
    elif 'Hrana' in d['category'][0] or 'Gastro' in d['category'][0]:
        kategorija='Hrana'
    elif 'Auti' in d['category'][0]:
        kategorija='Auti'
    elif 'Edukacije' in d['category'][0]:
        kategorija='Edukacije'
    elif 'Zabava' in d['category'][0]:
        kategorija='Zabava'
    elif 'Rekreacija' in d['category'][0] or 'rekreacija' in d['category'][0]:
        kategorija='Rekreacija'
    link=d['link'][0]
    link=link.strip()
    link=link
    title=""
    for t in d['title']:
        title=title+t
    title=title.strip()
    title=title.upper()
    img=d['src'][0]
    img=img.strip()
    img=img
    desc=""
    if d['desc']:
        desc=d['desc'][0]
        desc=desc.strip()
    kune=d['title'][0]
    if kune:
        cijena=re.findall(r'\d* kn',kune)
        if cijena:
            cijena=cijena[0]
            cijena=cijena.split("kn")
            if cijena:
                
                cijena=cijena[0]
    """
    if d['cijena']:
        cijena=d['cijena'][0]
        cijena=cijena.split("k")
        cijena=cijena[0]
        cijena=cijena.strip()
        cijena=int(cijena)
        if d['popust']:
            popust=d['popust'][0]
            popust=popust.split("%")
            popust=popust[0]
            popust=popust.strip()
            popust=int(popust)
            cijena=cijena-((cijena*popust)/100)
            
    """
        
    i=i+1
    db.ponude.save(
   {
     '_id': link,
     'title': title,
     'link': link,
     'img': img,
     'desc': desc,
                     'likes':0,
                     'counter':i,
                     'datetime':datetime.now(),
                     'kategorija':kategorija,
                     'cijena':cijena,
     'Web_Stranica':"kolektiva.hr",
     'random':random.randint(1,100000)
     
   }
)


for d in data_najjeftinije:
    kategorija="Nista"
    if 'Zdravlje' in d['category'][0]  or 'zdravlja' in d['category'][0]:
        kategorija='Zdravlje'
    elif 'travel' in d['link'][0]:
        kategorija='Putovanja'
    elif 'Hrana' in d['category'][0] or 'Gastro' in d['category'][0]:
        kategorija='Hrana'
    elif 'Autopraonice' in d['category'][0]:
        kategorija='Auti'
    elif 'Edukacije' in d['category'][0]:
        kategorija='Edukacije'
    elif 'ZABAVA' in d['category'][0]:
        kategorija='Zabava'
    elif 'Frizerski saloni' in d['category'][0]:
        kategorija='Ljepota'
    elif 'Rekreacija' in d['category'][0] or 'rekreacija' in d['category'][0]:
        kategorija='Rekreacija'
    link=d['link'][0]
    link=link.strip()
    link="http://najjeftinije.hr"+link
    title=""
    for t in d['title']:
        title=title+t
    title=title.strip()
    title=title.upper()
    img=d['src'][0]
    img=img.strip()
    img=img.split("') no-repeat")
    img=img[0].split("url('")
    img=img[1]
    
    desc=""
    
    cijena="Nepoznata"
    
   
        
    i=i+1
    db.ponude.save(
   {
     '_id': link,
     'title': title,
     'link': link,
     'img': img,
     'desc': desc,
                     'likes':0,
                     'counter':i,
                     'datetime':datetime.now(),
                     'kategorija':kategorija,
                     'cijena':cijena,
                     'Web_Stranica':"najjeftinije.hr",
     'random':random.randint(1,100000)
     
   }
)





for d in data_kupisve:
    kategorija="Nista"
    if 'ZDRAVLJE' in d['category'][0]  or 'zdravlja' in d['category'][0]:
        kategorija='Zdravlje'
    elif 'TURIZAM I PUTOVANJA' in d['link'][0]:
        kategorija='Putovanja'
    elif 'Hrana' in d['category'][0] or 'Gastro' in d['category'][0]:
        kategorija='Hrana'
    elif 'Autopraonice' in d['category'][0]:
        kategorija='Auti'
    elif 'Edukacije' in d['category'][0]:
        kategorija='Edukacije'
    elif 'ZABAVA' in d['category'][0]:
        kategorija='Zabava'
    elif 'LJEPOTA' in d['category'][0]:
        kategorija='Ljepota'
    elif 'SPORT I REKREACIJA' in d['category'][0] or 'rekreacija' in d['category'][0]:
        kategorija='Rekreacija'
    link=d['link'][0]
    link=link.strip()
    link="http://kupisve.eu"+link
    title=""
    for t in d['title']:
        title=title+t
    title=title.strip()
    title=title.upper()
    img=d['src'][0]
    img=img.strip()
    img=img.split("') no-repeat")
    img=img[0].split("url('")
    img=img[1]
    
    desc=""
    
    cijena="Nepoznata"
    
    
    
   
        
    i=i+1
    db.ponude.save(
   {
     '_id': link,
     'title': title,
     'link': link,
     'img': img,
     'desc': desc,
                     'likes':0,
                     'counter':i,
                     'datetime':datetime.now(),
                     'kategorija':kategorija,
                     'cijena':cijena,
     'Web_Stranica':"kupisve.eu",
     'random':random.randint(1,100000)
     
   }
)


for d in data_mojkupon:
    kategorija="Nista"
    if 'Zdravlje' in d['category'][0]  or 'zdravlja' in d['category'][0]:
        kategorija='Zdravlje'
    elif 'TURIZAM I PUTOVANJA' in d['link'][0]:
        kategorija='Putovanja'
    elif 'Hrana' in d['category'][0] or 'Gastro' in d['category'][0]:
        kategorija='Hrana'
    elif 'Autopraonice' in d['category'][0]:
        kategorija='Auti'
    elif 'Edukacije' in d['category'][0]:
        kategorija='Edukacije'
    elif 'Zabava' in d['category'][0]:
        kategorija='Zabava'
    elif 'Ljepota' in d['category'][0]:
        kategorija='Ljepota'
    elif 'SPORT I REKREACIJA' in d['category'][0] or 'rekreacija' in d['category'][0]:
        kategorija='Rekreacija'
    link=d['link'][0]
    link=link.strip()
    link="http://mojkupon.hr"+link
    title=""
    for t in d['title']:
        title=title+t
    title=title.strip()
    title=title.upper()
    img=d['src'][0]
    img=img.strip()
    
    
    desc=""
    if len(d['cijena'])>1:
        cijena=d['cijena'][1]
        cijena=cijena.split("kn")
        cijena=cijena[0]
    
    
    
   
        
    i=i+1
    db.ponude.save(
   {
     '_id': link,
     'title': title,
     'link': link,
     'img': img,
     'desc': desc,
                     'likes':0,
                     'counter':i,
                     'datetime':datetime.now(),
                     'kategorija':kategorija,
                     'cijena':cijena,
     'random':random.randint(1,100000)
     
   }
)


for d in data_kupizdravo:
    kategorija="Nista"
    if 'Poliklinke' in d['category'][0]  or 'zdravlja' in d['category'][0]:
        kategorija='Zdravlje'
    elif 'ponude' in d['link'][0]:
        kategorija='Putovanja'
    elif 'Hrana' in d['category'][0] or 'Gastro' in d['category'][0]:
        kategorija='Hrana'
    elif 'Autopraonice' in d['category'][0]:
        kategorija='Auti'
    elif 'Edukacije' in d['category'][0]:
        kategorija='Edukacije'
    elif 'Zabava' in d['category'][0]:
        kategorija='Zabava'
    elif 'Ljepota' in d['category'][0]:
        kategorija='Ljepota'
    elif 'SPORT I REKREACIJA' in d['category'][0] or 'rekreacija' in d['category'][0]:
        kategorija='Rekreacija'

    else:
        kategorija='Putovanja'
        
    link=d['link'][0]
    link=link.strip()
    link="http://www.kupizdravo.hr"+link
    title=""
    for t in d['title']:
        title=title+t
    title=title.strip()
    title=title.upper()
    img=d['src'][0]
    img=img.strip()
    
    
    desc=""
    vrijednost=d['dataorg'][0]
    vrijednost=vrijednost.split("kn")
    vrijednost=vrijednost[0]
    vrijednost=int(vrijednost)
    cijena=d['cijena'][0]
    cijena=cijena.split("kn")
    cijena=cijena[0]
    cijena=int(cijena)
    cijena=vrijednost-cijena
    
    
    
   
        
    i=i+1
    db.ponude.save(
   {
     '_id': link,
     'title': title,
     'link': link,
     'img': img,
     'desc': desc,
                     'likes':0,
                     'counter':i,
                     'datetime':datetime.now(),
                     'kategorija':kategorija,
                     'cijena':cijena,
     'Web_Stranica':"kupizdravo.hr",
     'random':random.randint(1,100000)
     
   }
)


for d in data_megapopust:
    kategorija="Nista"
    if 'Zdravlje i ljepota' in d['category'][0]  or 'zdravlja' in d['category'][0]:
        kategorija='Zdravlje'
    elif 'Putovanja:' in d['category'][0]:
        kategorija='Putovanja'
    elif 'Restorani:' in d['category'][0] or 'Gastro' in d['category'][0]:
        kategorija='Hrana'
    elif 'Najam vozila:' in d['category'][0]:
        kategorija='Auti'
    elif 'Edukacije' in d['category'][0]:
        kategorija='Edukacije'
    elif 'Sport i zabava:' in d['category'][0]:
        kategorija='Zabava'
    elif 'Zdravlje i ljepota' in d['category'][0]:
        kategorija='Ljepota'
    elif 'SPORT I REKREACIJA' in d['category'][0] or 'rekreacija' in d['category'][0]:
        kategorija='Rekreacija'

    
        
    link=d['link'][0]
    link=link.strip()
    link=link
    title=""
    for t in d['title']:
        title=title+t
    title=title.strip()
    title=title.upper()
    img=d['src'][0]
    img=img.strip()
    
    
    desc=""
    vrijednost=d['dataorg'][1]
    vrijednost=vrijednost.strip()
    vrijednost=vrijednost.split("kn")
    vrijednost=vrijednost[0]
    vrijednost=int(vrijednost)
    cijena=d['cijena'][0]
    cijena=cijena.split("kn")
    cijena=cijena[0]
    cijena=int(cijena)
    cijena=cijena-vrijednost
    
    
    
   
        
    i=i+1
    db.ponude.save(
   {
     '_id': link,
     'title': title,
     'link': link,
     'img': img,
     'desc': desc,
                     'likes':0,
                     'counter':i,
                     'datetime':datetime.now(),
                     'kategorija':kategorija,
                     'cijena':cijena,
     'Web_Stranica':"megapopust.hr",
     'random':random.randint(1,100000)
     
   }
)

for d in data_popustplus:
    kategorija="Nista"
    if 'categoryId=2' in d['category']:
        kategorija='Zdravlje'
    elif 'categoryId=1' in d['category']:
        kategorija='Putovanja'
    elif '&categoryId=5' in d['category'] :
        kategorija='Hrana'
    elif '&categoryId=8' in d['category']:
        kategorija='Auti'
    elif '&categoryId=4' in d['category']:
        kategorija='Edukacije'
    elif 'Sport i zabava:' in d['category']:
        kategorija='Zabava'
    elif '&categoryId=3' in d['category'] or "&categoryId=11" in d['category']:
        kategorija='Ljepota'
    elif '&categoryId=6' in d['category']:
        kategorija='Rekreacija'

    
        
    link=d['link'][0]
    link=link.strip()
    link="https://www.popustplus.hr"+link
    title=""
    for t in d['title']:
        title=title+t
    title=title.strip()
    title=title.upper()
    img=d['src'][0]
    img=img.strip()
    img="https://www.popustplus.hr"+img
    
    
    desc=""
    
    cijena=d['cijena'][0]
    cijena=cijena.split(",")
    cijena=cijena[0]
    
    
   
        
    i=i+1
    db.ponude.save(
   {
     '_id': link,
     'title': title,
     'link': link,
     'img': img,
     'desc': desc,
                     'likes':0,
                     'counter':i,
                     'datetime':datetime.now(),
                     'kategorija':kategorija,
                     'cijena':cijena,
     'Web_Stranica':"popustplus.hr",
     'random':random.randint(1,100000)
     
   }
)



for d in data_promotiva:
    kategorija="Nista"
    if 'categoryId=2' in d['category']:
        kategorija='Zdravlje'
    elif 'travel' in d['category'][0]:
        kategorija='Putovanja'
    elif '&categoryId=5' in d['category'] :
        kategorija='Hrana'
    elif '&categoryId=8' in d['category']:
        kategorija='Auti'
    elif '&categoryId=4' in d['category']:
        kategorija='Edukacije'
    elif 'Sport i zabava:' in d['category']:
        kategorija='Zabava'
    elif '&categoryId=3' in d['category'] or "&categoryId=11" in d['category']:
        kategorija='Ljepota'
    elif '&categoryId=6' in d['category']:
        kategorija='Rekreacija'

    
        
    link=d['link'][0]
    link=link.strip()
    link="http://www.promotiva.hr/"+link
    title=""
    for t in d['title']:
        title=title+t
    title=title.strip()
    title=title.upper()
    img=d['src'][0]
    img=img.strip()
    img="http://www.promotiva.hr/"+img
    
    
    desc=""
    
    cijena=d['cijena'][0]
    cijena=cijena.strip()
    cijena=cijena.split(",")
    cijena=cijena[0]
    
    
   
        
    i=i+1
    db.ponude.save(
   {
     '_id': link,
     'title': title,
     'link': link,
     'img': img,
     'desc': desc,
                     'likes':0,
                     'counter':i,
                     'datetime':datetime.now(),
                     'kategorija':kategorija,
                     'cijena':cijena,
     'Web_Stranica':"promotiva.hr",
     'random':random.randint(1,100000)
     
   }
)



print "Zavrsetak izvodenja skripte mongodb.py"
print "Spremljeno u bazu :"
print i
print "podataka!"



            
            
            
        
    
