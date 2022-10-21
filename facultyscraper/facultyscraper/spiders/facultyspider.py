from turtle import title
import scrapy

# Create an class for the faculty spider that inherits the scrapy spider characteristics
class FacultySpider(scrapy.Spider):
  # Create a name for the spider
  name = 'facultyspider'

  # URls we will be scraping
  start_urls = ['https://pages.charlotte.edu/connections/group/cci/']

  # Parse the page that is provide by the start_url. Get the names for each page. 
  def parse(self, response):
    for titles in response.css('h2.entry-title'):
      yield{
        'facultyName' : titles.css('a::text').get(),
      }

    # get the link for the next page. 
    next_page = response.css('a.nextpostslink').attrib['href']

    # If there is a next page for the website, follow it and callback the function to 
    # parse the page for the names
    if next_page is not None:
      yield response.follow(next_page, callback=self.parse)
