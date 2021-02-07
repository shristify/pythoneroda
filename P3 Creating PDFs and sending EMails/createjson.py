
#! /usr/bin/env python3
import os
import requests
import json
"""
this script adds book info instead of feedback,
to a service such as Library keeping or TBR 
"""
dir = "./data/books/"
data={}
data["books"]=[]
for file in os.listdir(dir): 
    format = ["genre","title","pages","author"]
    content = {}
    with open('{}/{}'.format(dir,file), 'r') as bookinfo:
        counter = 0
        for row in bookinfo:
            row = row.replace("\n", "")
            content[format[counter]] = row.strip('\n')
            counter += 1 
    print(content)
    data["books"].append(content)
"""
list of all lists
"""
with open('list.txt', 'w') as outfile:
    json.dump(data, outfile)
"""
converting text file into json file
"""
with open('book.json','w') as bookjson:
    json.dump(data, bookjson, indent=2)

