import scrapy
from scrapy.crawler import CrawlerProcess

# Create an class for the faculty spider that inherits the scrapy spider characteristics
class FacultySpider(scrapy.Spider):
  # Create a name for the spider
  name = 'facultyspider'

  # URls we will be scraping
  start_urls = ['https://cci.charlotte.edu/directory/faculty']

  # Parse the page that is provide by the start_url. Get the names for each page. 
  def parse(self, response):
    for titles in response.css('span.field-content'):
      yield{
        'facultyName' : titles.css('h3::text').get(),
      }

    # get the link for the next page. 
    next_page = response.css('li.next a::attr(href)').get()

    # If there is a next page for the website, follow it and callback the function to 
    # parse the page for the names
    if next_page is not None:
      yield response.follow(next_page, callback=self.parse)