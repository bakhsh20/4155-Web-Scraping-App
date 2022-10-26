import scrapy

# Scraper that scrapes department pages for raw HTML content about faculty.
class FacultyDescriptionSpider(scrapy.Spider):
  # Name of spider
  name = 'facultyDescriptionSpider'

  # Start URL of CCI department faculty page. 
  start_urls = ['https://cci.charlotte.edu/directory/faculty']

  
  # Get links for each of the page of the faculty member and scrapes data. 
  def parse(self, response):
    # Loop through each link for each faculty member
    for link in response.css('a.button.button-gray::attr(href)'):
      # Follow link. Callback function that scrapes faculty members page for information. 
      yield response.follow(link.get(), callback=self.parseFacultyPage)
        
      

  # Function that scrapes faculty members page for information. 
  def parseFacultyPage(self, response):
    # Creates object with properities for the name, title, descriptions...
      yield {
        'name' : response.css('h1.page-header::text').get(),
        'title' : response.css('div.field-name-field-directory-department').get(),
        'description': response.css('div.field.field-name-field-directory-biography').get(), 
      }
