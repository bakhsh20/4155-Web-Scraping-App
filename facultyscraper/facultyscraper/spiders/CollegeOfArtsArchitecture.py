import scrapy
from rake_nltk import Rake
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess

# Create rake_nltk object.
rake_nltk_var = Rake(
    min_length=1,
    max_length=3,
    include_repeated_phrases=False,
    language="english"
)

class ArtAndArtHistoryScraper(scrapy.Spider):
    name = 'ArtAndArtHistorySpider'

    # Start URL of department faculty page.
    start_urls = ['https://coaa.charlotte.edu/art/faculty-staff']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.thumbnail-link::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create temporary response object to be used for getting text field.
        tempTitle = response.css('div.field.field-name-field-directory-job-title')
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
            'department': 'Art & Art History',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }

class DanceScraper(scrapy.Spider):
    name = 'DanceSpider'

    # Start URL of department faculty page.
    start_urls = ['https://coaa.charlotte.edu/dance/faculty-staff']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.thumbnail-link::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create temporary response object to be used for getting text field.
        tempTitle = response.css('div.field.field-name-field-directory-job-title')
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
            'department': 'Dance',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }

class MusicScraper(scrapy.Spider):
    name = 'MusicSpider'

    # Start URL of department faculty page.
    start_urls = ['https://coaa.charlotte.edu/music/faculty-staff']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.thumbnail-link::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create temporary response object to be used for getting text field.
        tempTitle = response.css('div.field.field-name-field-directory-job-title')
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
            'department': 'Music',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }

class PerformingArtsScraper(scrapy.Spider):
    name = 'PerformingArtsSpider'

    # Start URL of department faculty page.
    start_urls = ['https://coaa.charlotte.edu/events-venues/performing-arts-services/staff']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.thumbnail-link::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create temporary response object to be used for getting text field.
        tempTitle = response.css('div.field.field-name-field-directory-job-title')
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
            'department': 'Performing Arts Services',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }

class ArchitectureScraper(scrapy.Spider):
    name = 'ArchitectureSpider'

    # Start URL of department faculty page.
    start_urls = ['https://coaa.charlotte.edu/architecture/faculty-staff']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.thumbnail-link::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create temporary response object to be used for getting text field.
        tempTitle = response.css('div.field.field-name-field-directory-job-title')
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
            'department': 'School of Architecture',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }

class TheatreScraper(scrapy.Spider):
    name = 'TheatreSpider'

    # Start URL of department faculty page.
    start_urls = ['https://coaa.charlotte.edu/theatre/faculty-staff']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.thumbnail-link::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create temporary response object to be used for getting text field.
        tempTitle = response.css('div.field.field-name-field-directory-job-title')
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
            'department': 'Theatre',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }
  
# Adjust crawler settings for the department.
process = CrawlerProcess(settings={
    "FEEDS": {
        "CollegeOfArtsArchitecture.csv": {"format": "csv"},

    },
})

# Call scrapers and run
process.crawl(ArtAndArtHistoryScraper)
process.crawl(DanceScraper)
process.crawl(MusicScraper)
process.crawl(PerformingArtsScraper)
process.crawl(ArchitectureScraper)
process.crawl(TheatreScraper)
process.start()