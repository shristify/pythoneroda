
#! /usr/bin/env python3
import os
import requests
"""
this script adds book info instead of feedback,
to a service such as Library keeping or TBR 
"""
dir = "./data/books/"
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

    #this data can be forwarded to generate pdf
    #response = requests.post("http://127.0.0.1:8000/addbooks/",json = content)  #post to the web service
    #if not response.ok:
    #    raise Exception("POST failed! |Status code: {} |File: {}".format(response.status_code, file))
    #print("Entry added!")
