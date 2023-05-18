# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:58:57 2023

@author: hanne
"""

# Read html
import json
import re

input_file = input("Name of R markdown file to convert: ")
input_file = input_file.replace(".html", "")
with open(input_file + ".html") as html_file:
    html = html_file.read()

# Get all the info from the document
def get_assay_title(html):
    result = re.search('<title>(.*)</title>', html)
    return(result.group(1))

def get_date(html):
    result = re.search('<meta name="date" content="(.*)-(.*)-(.*)" />', html)
    result = f'{result.group(3)}-{result.group(2)}-{result.group(1)}'
    return(result)

def get_description_or_purpose(html):
    pattern = r'<div id="description-or-purpose" class="section level1">(.*?)</div>\n<div id="results" class="section level1">'
    result = re.search(pattern, html,flags=re.DOTALL)
    return(result.group(1))

def get_results(html):
    pattern = r'<div id="results" class="section level1">(.*?)</div>\n<div id="conclusion" class="section level1">'
    result = re.search(pattern, html,flags=re.DOTALL)
    return(result.group(1))

def get_conclusion(html):
    pattern = r'<div id="conclusion" class="section level1">(.*?)</div>'
    result = re.search(pattern, html,flags=re.DOTALL)
    return(result.group(1))

# Read template
with open("SD241635.json", "r") as json_file:
    json_template = json.load(json_file)

# Extract template parts
for nr in range(0,len(json_template["fields"])):
    # Print information on the assay template format
    if json_template["fields"][nr]["name"] == "Assay Template Used":
        print("Putting data into json for assay version: " + json_template["fields"][nr]["content"])
    
    # Set the assay title
    if json_template["fields"][nr]["name"] == "Assay Title":
        result = get_assay_title(html)
        json_template["fields"][nr]["content"] = result
        
    # Set the assay date
    if json_template["fields"][nr]["name"] == "Date (dd-MM-yyyy)":
        result = get_date(html)
        json_template["fields"][nr]["content"] = result
    
    # Set the description or purpose
    if json_template["fields"][nr]["name"] == "Description or Purpose":
        result = get_description_or_purpose(html)
        json_template["fields"][nr]["content"] = result
        
    # Set the results
    if json_template["fields"][nr]["name"] == "Results":
        result = get_results(html)
        json_template["fields"][nr]["content"] = result
    
    # Set the conclusion
    if json_template["fields"][nr]["name"] == "Conclusion":
        result = get_conclusion(html)
        json_template["fields"][nr]["content"] = result
    
# Write to json
with open(input_file + ".json", "w") as json_file:
    json.dump(json_template, json_file)
    print("done")