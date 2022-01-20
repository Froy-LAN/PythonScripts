#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

URL = "https://crt.sh/?q=tryhackme.com" #'tryhackme.com' can be changed to any other domain
page = requests.get(URL)


with open('example.txt', "wb") as f:  #writes captured bytes into file to minimize requests
    f.write(page.content)             #comment away if file  with html content already exists

read_page = ''
with open('example.txt', 'rb') as f: #read captured bytes from file to minimize requests
    read_page = f.read()


soup = BeautifulSoup(read_page, "html.parser") #process the content in order fo look for certain tags
#print(soup)
tables = soup.find_all('table') #captur all tables
table = tables[2] #specify the third table, which is embedded within the second table

pre_subdomains = [] #pre-processed domain list
subdomains = []

pre_subdomains = table.find_all('td') # add all lines with a 'td' header

for line in pre_subdomains[4::7]:     #only add every 7th item beginning on the 4th spot, which is the column with subdomains in common name form
    print(line.text)                   #comment away if you do not want the shell output
    subdomains.append(str(line.text))  #add subdomains to list object for processed subdomains

with open('subsomains.txt', 'w') as f: #write subdomains to file
    for item in subdomains:
        f.write(item + '\n')
