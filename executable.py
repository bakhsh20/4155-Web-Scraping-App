#import OS package
import os

#install rake_nltk onto system for keyword processor
os.system('cmd /c "pip install rake_nltk"')

#install scrapy for scrapers
os.system('cmd /c "pip install scrapy"')

#navigate to venv and activate it 
os.chdir('./venv/Scripts')
os.system('cmd /c "activate"')

#Step back to root, then navigate to spiders folder
os.chdir('..')
os.chdir('..')
os.chdir('./facultyscraper/facultyscraper/spiders')


#run facultyspider, print to json
os.system('cmd /c "python -m scrapy crawl facultyspider -O  faculty.json"')

#run descriptions-spider, print to json
os.system('cmd /c "python -m scrapy crawl facultyDescriptionSpider -O descriptions.json"')


