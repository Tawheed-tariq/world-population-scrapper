import scrapy
from ..items import WorldPopulationItem

class WpSpider(scrapy.Spider):
    name = "wp"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        items = WorldPopulationItem()

        table = response.css('table#example2').css('tbody')
        rows = table.css('tr')
        for item in rows:
            
            row = item.css('td')
            country = row[1].css('::text').extract()
            population = row[2].css('::text').extract()
            land_area = row[6].css('::text').extract()
            world_share = row[11].css('::text').extract()

            items['country'] = country
            items['population'] = population
            items['land_area'] = land_area
            items['world_share'] = world_share
            yield items
        
        
