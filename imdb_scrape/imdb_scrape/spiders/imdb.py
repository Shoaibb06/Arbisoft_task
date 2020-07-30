import scrapy
from ..items import ImdbScrapeItem
import re

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top?ref_=nv_mv_250']

    def parse(self, response):
        movies_urls = response.css('.lister-list > tr > td.titleColumn > a::attr(href)' ).getall()

        for url in movies_urls:
            movie_url = response.urljoin(url)
            yield scrapy.Request(movie_url, callback=self.parse_movie_details)

    def parse_movie_details(self, response):
        movie = ImdbScrapeItem()
        rating_div = response.css('div.imdbRating')

        movie['rating_score'] = self.get_rating_score(rating_div)
        movie['rating_count'] = self.get_rating_count(rating_div)

        movie['genre'] = self.get_genre(response)

        movie_details_div = response.css('#titleDetails')

        movie['budget'] = self.get_budget(movie_details_div)
        movie['gross_usa'] = self.get_gross_usa(movie_details_div)

        yield movie

    #extracting rating score
    def get_rating_score(self,rating_div):
        rating_score = rating_div.css('div > strong > span::text').get()

        return rating_score

    #extracting total number of ratings
    def get_rating_count(self,rating_div):
        rating_count = rating_div.css('a > span::text').get()
        rating_count = rating_count.replace(',', '')
        return rating_count

    #extracting genre
    def get_genre(self, response):
        story_line_div = response.css('#titleStoryLine > div.see-more.inline.canwrap')
        genre = story_line_div[1].css('a::text').getall()

        return genre

    #extracting budget
    def get_budget(self, movie_details_div):
        budget = ''.join(movie_details_div.css(".txt-block:contains('Budget')::text").extract()).strip()
        movie_budget = ''.join(i for i in budget if i.isdigit()) or '0'

        return movie_budget

    #extracting gorss usa
    def get_gross_usa(self, movie_details_div):
        gross_usa = ''.join(movie_details_div.css(".txt-block:contains('Gross USA')::text").extract()).strip()
        movie_gross_usa = ''.join(i for i in gross_usa if i.isdigit()) or '0'

        return movie_gross_usa

