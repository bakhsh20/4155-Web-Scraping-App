#import OS package
import os
import nltk



#install rake_nltk onto system for keyword processor
os.system('cmd /c "pip install rake_nltk"')

#install scrapy for scrapers
os.system('cmd /c "pip install scrapy"')

#install beautifulsoup4
os.system('cmd /c "pip install beautifulsoup4"')

#install rake stopwords
os.system('cmd /c "Python -m nltk.downloader stopwords"')

#install punkt for rake
os.system('cmd /c "Python -m nltk.downloader punkt"')

#navigate to venv and activate it 
os.chdir('4155-Web-Scraping-App/venv/Scripts')
os.system('cmd /c "activate"')

#Step back to root, then navigate to spiders folder
os.chdir('..')
os.chdir('..')
os.chdir('./facultyscraper/facultyscraper/spiders')


#run CCIDepartmentSpider, print to json
os.system('cmd /c "python CCIDepartmentSpider.py"')

#run descriptions-spider, print to json
#os.system('cmd /c "python -m scrapy crawl facultyDescriptionSpider -O descriptions.json"')

