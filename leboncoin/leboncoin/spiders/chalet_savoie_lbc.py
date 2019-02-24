import scrapy
import time


class LbcSpider(scrapy.Spider):
    name = "chalet_savoie_lbc"
    start_urls = [
        'https://www.leboncoin.fr/voitures/offres/ile_de_france/',
        ]

def parse(self, response):
    for annonce in response.css('a.clearfix.trackable'):
        yield {
            'titre': annonce.css('p._2tubl').extract_first(),
            }
        #print(annonce.css('h2.item_title::text'))
        #print(annonce.css('h3.item_price::text'))
        #print(annonce.css('p.item_supp::text'))
        time.sleep(0.5)
