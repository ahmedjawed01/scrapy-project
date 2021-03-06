from scrapy.item import Item, Field

class CraigslistSampleItem(Item):
	Heading = Field()
	Description = Field()
	Street_name = Field()
	House_number = Field()
	Rent = Field()
	Rental_period_id = Field()
	Available = Field()
	Rooms = Field()
	Zip_code_code = Field()
	Property_type = Field()
	Deposit_numb = Field()
	Area = Field()
	Images = Field()
	external_property_attributes = Field()
	external_provider_id = Field()
	external_property_id = Field()
	external_property_id = Field()
	property_url = Field()
