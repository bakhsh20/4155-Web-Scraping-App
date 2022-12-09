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

class CounselingScraper(scrapy.Spider):
    # Name of spider
    name = 'CounselingSpider'

    # Start URL of department faculty page.
    start_urls = ['https://education.charlotte.edu/directory/21']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('td.views-field.views-field-field-directory-read-more-link'):
            # Create a finalLink to follow
            finalLink = link.css('a::attr(href)')
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(finalLink.get(), callback=self.parseFacultyPage)

    # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
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
            'department' : 'Counseling',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }

class EducationalLeadershipScraper(scrapy.Spider):
    # Name of spider
    name = 'EducationalLeadershipScraper'

    # Start URL of department faculty page.
    start_urls = ['https://education.charlotte.edu/directory/23']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('td.views-field.views-field-field-directory-read-more-link'):
            # Create a finalLink to follow
            finalLink = link.css('a::attr(href)')
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(finalLink.get(), callback=self.parseFacultyPage)

    # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
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
            'department' : 'Educational Leadership',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }


class MDSKScraper(scrapy.Spider):
    # Name of spider
    name = 'MDSKDepartment'

    # Start URL of department faculty page.
    start_urls = ['https://education.charlotte.edu/directory/middle-secondary']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('td.views-field.views-field-field-directory-read-more-link'):
            # Create a finalLink to follow
            finalLink = link.css('a::attr(href)')
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(finalLink.get(), callback=self.parseFacultyPage)

    # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
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
            'department' : 'MDSK Department',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }


class SPCDScraper(scrapy.Spider):
    # Name of spider
    name = 'SPCDSpider'

    # Start URL of department faculty page.
    start_urls = ['https://education.charlotte.edu/directory/special-education']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('td.views-field.views-field-field-directory-read-more-link'):
            # Create a finalLink to follow
            finalLink = link.css('a::attr(href)')
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(finalLink.get(), callback=self.parseFacultyPage)

    # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
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
            'department' : 'MDSK Department',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }

class REELScraper(scrapy.Spider):
    # Name of spider
    name = 'REELSpider'

    # Start URL of department faculty page.
    start_urls = ['https://education.charlotte.edu/directory/27']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('td.views-field.views-field-field-directory-read-more-link'):
            # Create a finalLink to follow
            finalLink = link.css('a::attr(href)')
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(finalLink.get(), callback=self.parseFacultyPage)

    # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
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
            'department' : 'REEL Department',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }


# Adjust crawler settings for the department.
process = CrawlerProcess(settings={
    "FEEDS": {
        "CollegeOfEducation.csv": {"format": "csv"},

    },
})

# Call Scrapers and run
process.crawl(CounselingScraper)
process.crawl(EducationalLeadershipScraper)
process.crawl(MDSKScraper)
process.crawl(SPCDScraper)
process.crawl(REELScraper)
process.start()