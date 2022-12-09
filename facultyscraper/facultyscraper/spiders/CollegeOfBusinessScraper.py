import scrapy
from scrapy.crawler import CrawlerProcess
from rake_nltk import Rake
from bs4 import BeautifulSoup

# Rake NLTK setting adjustments
rake_nltk_var = Rake(
    min_length=1,
    max_length=3,
    include_repeated_phrases=False,
    language="english"
)

# ALL OF THE FACULTY AT THE COLLEGE OF BUSINESS ARE UNDER ONE PAGE
class BusinessScraper(scrapy.Spider):
    name = 'BusinessScraper'

    # Start URL of department faculty page.
    start_urls = ['https://belkcollege.charlotte.edu/directory?title=&tid_1=All&tid=All']

    # Get links for each of the page of the faculty member and scrapes data.
    def parse(self, response):
        # Loop through each link for each faculty member
        for link in response.css('a.button.button-gray::attr(href)'):
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
            'department': 'Business',
            'name': response.css('h1.page-header::text').get(),
            'title': tempTitle.css('div.field-item::text').get(),
            'description': keywordList
        }


# Adjust crawler settings for the Liberal Arts College.
process = CrawlerProcess(settings={
    "FEEDS": {
        "CollegeOfBusiness.csv": {"format": "csv"},

    },
})

# Call scrapers and run
process.crawl(BusinessScraper)
process.start()