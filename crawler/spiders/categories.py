import scrapy
from scrapy.http import Request
from crawler.items import ProductItem


class CategoriesSpider(scrapy.Spider):
    name = 'categories'
    allowed_domains = ['kolonial.no']
    start_urls = ['https://kolonial.no/kategorier']
    base_url = 'https://' + allowed_domains[0]

    # Gets all the categories
    def parse(self, response):
        categories = response.css(
            ('.filter-sidebar .navbar-collapse '
             '.parent-category h4 a::attr(href)')).extract()

        categories = categories[2:]

        for category in categories:
            yield Request(url=self.base_url + category,
                          callback=self.parse_category)

    # Gets all the subcategories of a given category
    def parse_category(self, response):
        subcategories = response.css(
            ('.filter-sidebar .parent-category '
             '.child-category a::attr(href)')).extract()
        for subcategory in subcategories:
            yield scrapy.Request(self.base_url + subcategory,
                                 callback=self.parse_subcategory)

    # Proceeds to the subcategory page and extract information
    def parse_subcategory(self, response):
        items = response.css('.product-category-list .product-list-item')

        sidebar = response.css('.filter-sidebar')

        category = (response
                    .css('li.parent-category.active '
                         '.aggregation-filter-headline '
                         'a::text')).extract_first()
        subcategory = (sidebar
                       .css('.child-category '
                            '.active .category-name::text').extract_first())

        for item in items:
            main_name = item.css('.name-main::text').extract_first()
            extra_name = item.css('.name-extra::text').extract_first()
            price = item.css('.price::text').extract_first()
            unit_price = item.css('.unit-price::text').extract_first()
            not_available = item.css('.product-list-item .not-for-sale').extract_first()
            if not_available:
                continue

            product = ProductItem()

            product['main_name'] = self.clean_data(main_name)
            product['extra_name'] = self.clean_data(extra_name)
            product['price'] = self.clean_data(price)
            product['unit_price'] = self.clean_data(unit_price)
            product['subcategory'] = self.clean_data(subcategory)
            product['category'] = self.clean_data(category)

            yield product

        next_page = (response
                     .css('.pagination '
                          'a[title="Neste side"]::attr(href)').extract_first())
        if next_page:
            yield Request(response.url + next_page,
                          callback=self.parse_subcategory)

    # Remove whitespaces/tabs/new lines
    def clean_data(self, data):
        data = data.lstrip()
        data = data.rstrip()
        return data
