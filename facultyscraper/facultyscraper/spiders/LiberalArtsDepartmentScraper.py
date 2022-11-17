import scrapy
from scrapy.crawler import CrawlerProcess
from rake_nltk import Rake
from bs4 import BeautifulSoup

rake_nltk_var = Rake(
    min_length=1,
    max_length=3,
    include_repeated_phrases=False,
    language="english"
)

class BiologyScraper(scrapy.Spider):
    name = 'BiologySpider'

    # Start URL of CCI department faculty page.
    start_urls = ['https://biology.charlotte.edu/directory/faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('div.caption a::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create temporary response object to be used for getting text field.
        tempTitle = response.css('div.field-name-field-directory-department')
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.field.field-name-field-directory-biography')

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.css(
            'div.field-item').get()).get_text()

        # Extract keywords from the text content of each biography section
        rake_nltk_var.extract_keywords_from_text(text)

        # Create a keyword list for each biography section.
        keywords = rake_nltk_var.get_ranked_phrases_with_scores()

        # Remove words with a low ranking in score and input into new list
        keywordList = []

        for i in keywords:
            if i[0] >= 3.5:
                keywordList.append(i[1])

        # Creates object with properities for the name, title, descriptions(which is keyword list)...
        yield {
            'department' : 'biology',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }

class ChemistryScraper(scrapy.Spider):
    name = 'ChemistrySpider'

    # Start URL of CCI department faculty page.
    start_urls = ['https://chemistry.charlotte.edu/directory-grid/faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.thumbnail-link::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create temporary response object to be used for getting text field.
        tempTitle = response.css('div.field-name-field-directory-department')
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.field.field-name-field-directory-biography')

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.css('div.field-item').get()).get_text()

        # Extract keywords from the text content of each biography section
        rake_nltk_var.extract_keywords_from_text(text)

        # Create a keyword list for each biography section.
        keywords = rake_nltk_var.get_ranked_phrases_with_scores()

        # Remove words with a low ranking in score and input into new list
        keywordList = []

        for i in keywords:
            if i[0] >= 3.5:
                keywordList.append(i[1])

        # Creates object with properities for the name, title, descriptions(which is keyword list)...
        yield {
            'department' : 'chemistry',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }


# Adjust crawler settings for the chemistry department.
process = CrawlerProcess(settings={
    "FEEDS": {
        "LiberalArts.csv": {"format": "csv"},

    },
})

process.crawl(BiologyScraper)
process.crawl(ChemistryScraper)
process.start()




