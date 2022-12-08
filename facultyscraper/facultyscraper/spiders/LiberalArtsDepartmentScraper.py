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

    # Start URL of department faculty page.
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
            'department': 'biology',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }


class ChemistryScraper(scrapy.Spider):
    name = 'ChemistrySpider'

    # Start URL of department faculty page.
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
            'department': 'chemistry',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }


class CommunicationsScraper(scrapy.Spider):
    name = 'CommunicationsSpider'

    # Start URL of department faculty page.
    start_urls = [
        'https://communication.charlotte.edu/people/full-time-faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-gray::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.details')

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.get()).get_text()

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
            'department': 'Communications',
            'name': response.css('div.name::text').get(),
            'title': "",
            'description': keywordList
        }


class CriminalJusticeScraper(scrapy.Spider):
    name = 'CriminalJusticeSpider'

    # Start URL of department faculty page.
    start_urls = ['https://criminaljustice.charlotte.edu/people/faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-gray::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.details')

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.get()).get_text()

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
            'department': 'Criminal Justice and Criminology',
            'name': response.css('div.name::text').get(),
            'title': "",
            'description': keywordList
        }

class EnglishScraper(scrapy.Spider):
    name = 'EnglishSpider'

    # Start URL of department faculty page.
    start_urls = ['https://english.charlotte.edu/directory-list/professorial-faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-gray::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.details')

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.get()).get_text()

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
            'department': 'English',
            'name': response.css('div.name::text').get(),
            'title': "",
            'description': keywordList
        }

class HistoryScraper(scrapy.Spider):
    name = 'HistoryScraper'

    # Start URL of department faculty page.
    start_urls = ['https://history.charlotte.edu/people/faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.thumbnail-link::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.details')

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.get()).get_text()

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
            'department': 'History',
            'name': response.css('div.name::text').get(),
            'title': "",
            'description': keywordList
        }

class MathematicsAndStatisticsScraper(scrapy.Spider):
    # Name of spider
    name = 'MathAndStatSpider'

    # Start URL of department faculty page.
    start_urls = ['https://math.charlotte.edu/directory-list/faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-gray::attr(href)'):
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
            'department' : 'Mathematics and Statistics',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }

class PoliticalScienceScraper(scrapy.Spider):
    # Name of spider
    name = 'PoliticalScienceSpider'

    # Start URL of department faculty page.
    start_urls = ['https://politicalscience.charlotte.edu/directory-list/full-time-faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-gray::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.followLink) 
    
    # Follow the secondary link on the page. This takes you to the faculty page that is on the department page. 
    def followLink(self, response):
        temp1 = response.css('div.field.field-name-field-directory-biography')
        temp2 = temp1.css('div.field-items')
        temp3 = temp2.css('div.field-item.even')
        finalLink = temp3.css('a::attr(href)')
        yield response.follow(finalLink.get(), callback=self.parseFacultyPage)

    # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.details')

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.get()).get_text()

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
            'department' : 'Political Science',
            'name': response.css('div.name::text').get(),
            'title': "",
            'description': keywordList
        }

class PhilosophyScraper(scrapy.Spider):
    name = 'PhilosophySpider'

    # Start URL of department faculty page.
    start_urls = ['https://philosophy.charlotte.edu/directory-list/faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-gray::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.details')

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.get()).get_text()

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
            'department': 'Philosophy',
            'name': response.css('div.name::text').get(),
            'title': "",
            'description': keywordList
        }

class SociologyScraper(scrapy.Spider):
    name = 'PhilosophySpider'

    # Start URL of department faculty page.
    start_urls = ['https://sociology.charlotte.edu/directory-list/full-time-faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-gray::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

      # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.details')

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.get()).get_text()

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
            'department': 'Sociology',
            'name': response.css('div.name::text').get(),
            'title': "",
            'description': keywordList
        }

class GeoEarthScraper(scrapy.Spider):
    name = 'GeoEarthSpider'

    # Start URLs of the department page
    start_urls = ['https://geoearth.charlotte.edu/directory-flip/full-time-faculty']

    # Parse through each faculty card and pull information
    def parse(self,response):
        for section in response.css('div.directory-front'):
            yield {
                'department' : "Geography and Earth Sciences",
                'name' : section.css('h2.heading-med::text').get(),
                'title' : section.css('div.directory-job-title::text').get(),
                'description' : section.css('div.directory-department::text').get(),
                

            }

class PhysicsAndOpticalScienceScraper(scrapy.Spider):
    # Name of spider
    name = 'PhysicsSpider'

    # Start URL of department faculty page.
    start_urls = ['https://physics.charlotte.edu/people']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('div.directory-back'):
            # Create link to follow, second 'a href' inside the div. 
            finalLink = link.css('a::attr(href)')[1]
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
            'department' : 'Physics and Optical Sciences',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }

class PsychologicalStudiesScraper(scrapy.Spider):
    # Name of spider
    name = 'PsychologicalStudiesSpider'

    # Start URL of department faculty page.
    start_urls = ['https://psych.charlotte.edu/people']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('div.directory-back'):
            # Create link to follow, second 'a href' inside the div. 
            finalLink = link.css('a::attr(href)')[1]
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
            'department' : 'Psychological Studies',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }

class GlobalStudiesScraper(scrapy.Spider):
    # Name of spider
    name = 'GlobalStudiesSpider'

    # Start URL of department faculty page.
    start_urls = ['https://globalstudies.charlotte.edu/people']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('div.directory-back'):
            # Create link to follow, second 'a href' inside the div. 
            finalLink = link.css('a::attr(href)')[1]
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(finalLink.get(), callback=self.parseFacultyPage)

    # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.field.field-name-body')

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
            'department' : 'Psychological Studies',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }

class LanguageStudiesScraper(scrapy.Spider):
    # Name of spider
    name = 'LanguageStudiesSpider'

    # Start URL of department faculty page.
    start_urls = ['https://languages.charlotte.edu/people']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('div.directory-back'):
            # Create link to follow, second 'a href' inside the div. 
            finalLink = link.css('a::attr(href)')[1]
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
            'department' : 'Language and Cultural Studies',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }


class WritingRhetoricStudies(scrapy.Spider):
    name = 'WritingRhetoricSpider'

    # Start URL of department faculty page.
    start_urls = ['https://writing.charlotte.edu/directory-grid/faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.thumbnail-link::attr(href)'):
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(link.get(), callback=self.parseFacultyPage)

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
            'department': 'Writing, Rhetoric and Digital Studies',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }

class AnthropologyScraper(scrapy.Spider):
    # Name of spider
    name = 'AnthropologySpider'

    # Start URL of department faculty page.
    start_urls = ['https://anthropology.charlotte.edu/people']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('div.directory-back'):
            # Create link to follow, second 'a href' inside the div. 
            finalLink = link.css('a::attr(href)')[1]
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
            'department' : 'Anthropology',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }

class AfricanStudiesScraper(scrapy.Spider):
    # Name of spider
    name = 'AfricanaStudiesSpider'

    # Start URL of department faculty page.
    start_urls = ['https://africana.charlotte.edu/people/full-time-faculty']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('div.directory-back'):
            # Create link to follow, second 'a href' inside the div. 
            finalLink = link.css('a::attr(href)')[1]
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(finalLink.get(), callback=self.parseFacultyPage)

    # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.field.field-name-body')

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
            'department' : 'Africana Studies',
            'name': response.css('h1.page-header::text').get(),
            'title': "",
            'description': keywordList
        }

class ReligiousStudiesScraper(scrapy.Spider):
    # Name of spider
    name = 'ReligiousStudiesSpider'

    # Start URL of department faculty page.
    start_urls = ['https://religiousstudies.charlotte.edu/directory/faculty-and-staff']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('div.directory-back'):
            # Create link to follow, second 'a href' inside the div. 
            finalLink = link.css('a::attr(href)')[1]
            # Follow link. Callback function that scrapes faculty members page for information.
            yield response.follow(finalLink.get(), callback=self.parseFacultyPage)
          # Function that scrapes faculty members page for information.
    def parseFacultyPage(self, response):
        # Create tempDescription to refine search for correct HTML
        tempDescription = response.css(
            'div.details')

        # Clean the raw html to text
        text = BeautifulSoup(tempDescription.get()).get_text()

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
            'department': 'Religious Studies',
            'name': response.css('div.name::text').get(),
            'title': "",
            'description': keywordList
        }

# Adjust crawler settings for the Liberal Arts College.
process = CrawlerProcess(settings={
    "FEEDS": {
        "LiberalArts.csv": {"format": "csv"},

    },
})

process.crawl(AfricanStudiesScraper)
process.crawl(AnthropologyScraper)
process.crawl(BiologyScraper)
process.crawl(ChemistryScraper)
process.crawl(CommunicationsScraper)
process.crawl(CriminalJusticeScraper)
process.crawl(EnglishScraper)
process.crawl(GeoEarthScraper)
process.crawl(GlobalStudiesScraper)
process.crawl(HistoryScraper)
process.crawl(LanguageStudiesScraper)
process.crawl(MathematicsAndStatisticsScraper)
process.crawl(PhilosophyScraper)
process.crawl(PhysicsAndOpticalScienceScraper)
process.crawl(PoliticalScienceScraper)
process.crawl(PsychologicalStudiesScraper)
process.crawl(ReligiousStudiesScraper)
process.crawl(SociologyScraper)
process.crawl(WritingRhetoricStudies) 
process.start()
