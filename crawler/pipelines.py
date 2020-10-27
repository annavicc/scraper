from datetime import datetime
from scrapy.exporters import CsvItemExporter


class CrawlerPipeline:

    def __init__(self):
        current_date = datetime.today().strftime('%Y-%m-%d')
        self.filename = './results/products-%s.csv' % current_date

    def open_spider(self, spider):
        self.file = open(self.filename, 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
