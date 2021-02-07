#!/usr/bin/env python3

import emails
import reports 
import json
import os
import createjson
from datetime import datetime
import sys

def load_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data   

def process_data(data):
    now = datetime.now()
    summary=["Number of books in record now is {}.".format((len(data['books']))), "Year 2021", "Month: {}".format(now.strftime('%B'))]
    return summary


def books_dict_to_table(book_data):
    table_data = [["genre","title","pages","author"]]
    for item in book_data["books"]:
        table_data.append([item["genre"],item["title"], item["pages"], item["author"]])
    return table_data


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("book.json")
    summary = process_data(data)
    filename = "./tmp/books.pdf"
    title = "TBR/Reading List 2021"
    additional_info = "<br/>".join(summary)  
    table_data = books_dict_to_table(data)
    reports.generate(filename, title, additional_info, table_data)
    sender = "asteroidbyjava007@gmail.com"
    recipient = "********"  #receiver mail
    subject = "TBR/Reading List 2021"
    body = "\n".join(summary)
    attachment_path = "./tmp/books.pdf"
    message = emails.generate(sender, recipient, subject, body, attachment_path)
    emails.send(message)
    #print("EMAIL OK") # test
  
if __name__ == "__main__":
    main(sys.argv)
