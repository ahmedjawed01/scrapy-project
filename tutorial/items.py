from scrapy.item import Item, Field

class DmozItem(Item):
    title = Field()
    link = Field()
    desc = Field()
    category = Field()
    dataorg = Field()
    src = Field()
    cijena = Field()
    popust = Field()
