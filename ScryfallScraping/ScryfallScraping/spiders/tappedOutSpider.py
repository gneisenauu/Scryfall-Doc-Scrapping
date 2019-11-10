# -*- coding: utf-8 -*-
import scrapy
from ..items import ScryfallscrapingItem #import class from another directory

class TappedoutspiderSpider(scrapy.Spider):
	#to run: use 'scrapy crawl tappedOutSpider -o output.json' << writes output to json file
	#note: TODO: delete output.json after process is complete, otherwise file gets overwritten
	name = 'tappedOutSpider'

	start_urls = ['http://tappedout.net/mtg-decks/scraper-sample/?cb=1573109637']
	# start_urls = ['http://tappedout.net/mtg-decks/yawgmoth-zombiesish/'] #TEMPORARY. Todo: get custom url from helper function

	def parse(self, response):
		items = ScryfallscrapingItem() #stores instance of our ScryfallscrapingItem's class
		
		my_card_name = response.css('.card-hover::text').extract() #if you do not include ::text, you will extract the tag, not the text
        #Note: for images, the above will not select images. It will select the element in which the image is contained.
        #	add ::attr(src) attribute to obtain image
		
		items['card_name'] = my_card_name
        
		yield items