from scrapy import Field, Item


class ProductItem(Item):
    main_name = Field()
    extra_name = Field()
    unit_price = Field()
    price = Field()
    category = Field()
    subcategory = Field()
