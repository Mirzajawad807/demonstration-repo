#!/usr/bin/env python3
import json

# Reading json file
file = open('hlp-base-amazoncorretto.json')
json_data = json.loads(file.read())

# Creating Packages list text file
file_path = 'scanned_packages_list.txt'

# Adding header in packages list file
headers = 'Scanned Packages \n================ \n \n'


# Recording Packages and version of softwares
with open(file_path, 'w') as data:
  data.write(headers)
  for name in json_data["softwares"]:
    package_data = name["name"] + " == " + name["version"]
    data.write(package_data + '\n')
