import json

# Open JSON file
with open('facultyscraper/cciFaculty.json', 'r') as json_file:
  data = json.load(json_file)


print("Type:" , type(data))


for val in data:
  # Must write as *val.values to get each name unpacked as just the name. 
  print(*val.values())


