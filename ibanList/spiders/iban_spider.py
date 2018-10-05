import scrapy
import copy
from ..items import IBANItem

class IBANSpider(scrapy.Spider):
    name = "iban"
    BASE_URL = "https://www.xe.com"
    ENDPOINT = "/ibancalculator/countrylist/"
    start_urls = [
        "{}{}".format(BASE_URL, ENDPOINT)
    ]

    def parse(self, response):
        country_list = response.css("#country-list > li.list-tile")
        for country in country_list:
            detail_url = country.css("a::attr(href)").extract_first().strip()
            flag_url = country.css("a > img::attr(src)").extract_first().strip()
            name = country.css("a > span.list-item-text > span.search-text::text").extract_first().strip()

            item = IBANItem(name=name, detail_url=detail_url, flag_url=[response.urljoin(flag_url)])

            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'country': item})

    def parse_detail(self, response):
        country = response.meta['country']

        d = dict()
        table = response.css("table.ibanTable")[0]
        k, v = table.css("tr > th::text").extract()
        d[k] = v
        lines = table.css("tr > td")
        keys = lines.css(":nth-child(1)")
        values = lines.css(":nth-child(2)")
        length = min(len(keys), len(values))
        keys, values = (keys[:length], values[:length])
        keys = keys.css("::text").extract()
        values = values.css("::text").extract()
        for k, v in zip(keys, values):
            d[k] = v
        self.log(d)

        country['data'] = d
        yield country
