from rake_nltk import Rake

# Create a processor object. Min length is minimum amount of words to process as a key, max is the maximimum
# amount of words to process as key. Doesnt repeat phrases
rake_nltk_var = Rake(min_length=1 , max_length=3, include_repeated_phrases=False)

# HTML text pulled from faculty website. 
text = """<div class="field field-name-field-directory-biography field-type-text-with-summary field-label-hidden"><div class="field-items"><div class="field-item even"><p><strong>Personal Website:\xa0</strong><a href="http://webpages.uncc.edu/bcukic/">http://webpages.uncc.edu/bcukic/</a></p>\n\n<p>Dr. Bojan Cukic is a Professor and Interim Dean in the College of Computing and Informatics\xa0at the University of North Carolina at Charlotte.\xa0 He previously served as Associate Dean for Academic Programs and Student Success as well as the Chair of the Department of Computer Science and the Interim Executive Director of the UNC Charlotte\xa0Data Science Initiative.\xa0\xa0Dr. Cukic’s research interests include information assurance and biometrics, software engineering with emphasis on verification and validation, and resilient computing.\xa0\xa0He received MS and PhD degrees in Computer Science from the University of Houston, and holds an honorary doctorate from the University of Rijeka, Croatia.</p>\n\n<p>Dr. Cukic received a National Science Foundation Career award. His research was recognized with the Tycho Brahe award from NASA Office of Safety and Mission Assurance.\xa0He often collaborates with industry and has\xa0served as\xa0the director of the\xa0Center for Identification Technology Research (CITeR), an NSF Industry University Cooperative Research Center.\xa0 He co-founded a startup, NexID Biometrics Inc., subsequently acquired by Precise Biometrics.\xa0</p>\n</div></div></div>"""

# Pulls keyworkds from text
rake_nltk_var.extract_keywords_from_text(text)

# Store keywords as a list inside 'keywords'
keywords = rake_nltk_var.get_ranked_phrases()

# print list
print(keywords)
