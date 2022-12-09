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


# Scraper that scrapes department pages for raw HTML content about faculty.
class CivEnvironScraper(scrapy.Spider):
    # Name of spider
    name = 'CivEnvironment'

    # Start URL of Civil/Environmental Engdepartment faculty page.
    start_urls = ['https://cee.charlotte.edu/directory-box']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-green.button-small::attr(href)'):
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
            'department' : 'Civil Engineering',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }

class ElecCompScraper(scrapy.Spider):
    # Name of spider
    name = 'ElecComp'

    # Start URL of Civil/Environmental Engdepartment faculty page.
    start_urls = ['https://ece.charlotte.edu/directory/faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-green.button-small::attr(href)'):
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
            'department' : 'Electrical and Computer Engineering',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }

class TechConstScraper(scrapy.Spider):
    # Name of spider
    name = 'TechConst'

    # Start URL of Civil/Environmental Engdepartment faculty page.
    start_urls = ['https://et.charlotte.edu/about-us/faculty-and-staff-directory']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-green.button-small::attr(href)'):
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
            'Department' : 'Engineering Technology',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }

class MechEngScraper(scrapy.Spider):
    # Name of spider
    name = 'MechEng'

    # Start URL of Civil/Environmental Engdepartment faculty page.
    start_urls = ['https://mees.charlotte.edu/directory/faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-green.button-small::attr(href)'):
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
            'department' : 'Mechanical Engineering',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }

class SysEngScraper(scrapy.Spider):
    # Name of spider
    name = 'SysEng'

    # Start URL of Civil/Environmental Engdepartment faculty page.
    start_urls = ['https://seem.charlotte.edu/directory-box']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-green.button-small::attr(href)'):
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
            'department' : 'Systems Engineering and Engineering Management',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }

# Adjust crawler settings for the department.
process = CrawlerProcess(settings={
    "FEEDS": {
        "EngDept.csv": {"format": "csv"},

    },
})

process.crawl(CivEnvironScraper)
process.crawl(ElecCompScraper)
process.crawl(TechConstScraper)
process.crawl(MechEngScraper)
process.crawl(SysEngScraper)
process.start()