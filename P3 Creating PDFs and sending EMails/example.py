#!/usr/bin/env python3

import os
import reports 
import emails

table_data=[
  ["fruit","number","calories"],
  ['elderberries', 10, 0.45],
  ['figs', 5, 3],
  ['apples', 4, 2.75],
  ['durians', 1, 25],
  ['bananas', 5, 1.99],
  ['cherries', 23, 5.80],
  ['grapes', 13, 2.48],
  ['kiwi', 4, 0.49]]
reports.generate("./tmp/fruits.pdf", "A Complete Inventory of My Fruit", "This is all my fruit.", table_data)
sender = "asteroidbyjava007@gmail.com"
recipient = "******" #recipient mail
subject = "FRUIT INVENTORY"

body = "MY FRUIT LIST"
attachment_path = "./tmp/fruits.pdf"
message = emails.generate(sender, recipient, subject, body, attachment_path)
emails.send(message)
