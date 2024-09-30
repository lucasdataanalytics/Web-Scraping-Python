import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/data-science"]

    def parse(self, response):
        products = response.css('div.ui-search-result__content')
        
        for product in products:
            yield{
                'name': products.css('h2.ui-search-item__title.ui-search-item__group__element a::text').get()
                }