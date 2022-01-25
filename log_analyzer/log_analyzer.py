#!/usr/bin/env python3
import re
import operator
import csv
from collections import OrderedDict    #imported in case environment does default to ordered dictionaries


error = {}
per_user = {}


with open('syslog.log') as f:       #read entries from log file titled 'syslog.log'
    log = f.readlines()

for line in log:
    log[log.index(line)] = line.strip()    #remove any unnecessary spaces at either end of the line


pattern = r"(ERROR|INFO) ([ 'a-zA-Z]*)\[?#?\d?\d?\d?\d?\]? \(([\w.]*)\)" #pattern that recognizes entry type, content message, and username

for line in log:

    x = re.search(pattern, line)        #extract the pattern groups from each entry
    if x.group(1) == "ERROR":           #if the entry is an ERROR entry, perform the following

        if x.group(2) not in error:       #Increase count of error type
            error[x.group(2)] = 1
        else:
            error[x.group(2)] += 1

        if x.group(3) not in per_user:     #increase the number of error entries per user
            per_user[x.group(3)] = [0, 1]
        else:
            per_user[x.group(3)] = [per_user.get(x.group(3))[0], per_user.get(x.group(3))[1] + 1]

    else:  #if the entry is an INFO entry, perform the following

        if x.group(3) not in per_user:       #increase the number of info type entries per user
            per_user[x.group(3)] = [1, 0]
        else:
            per_user[x.group(3)] = [per_user.get(x.group(3))[0] + 1, per_user.get(x.group(3))[1]]


sorted_error = {}     #create ordered dictionary objects so all entries retain their placement
sorted_user = {}

for item in (sorted(per_user.items(), key=operator.itemgetter(0))): #sort dictionary with number of each type of entry (INFO|ERRO)
    sorted_user[item[0]] = item[1]                                  #to be ordered alphabetically

for item in (sorted(error.items(), key=operator.itemgetter(1), reverse=True)): #sort dictionary with count of error type to be sorted
    sorted_error[item[0]] = item[1]                                            #from the highest to lowest number

with open('user_statistics.csv', 'w', newline='') as file:                                #create filed called 'user_statistics.csv'
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)    #add number of entries per type to it
    writer.writerow(["Username", "INFO", "ERROR"])
    for key, value in sorted_user.items():
        writer.writerow([key, value[0], value[1]])

with open('error_message.csv', 'w', newline='') as file:                                  #create file calld 'error_messages.csv'
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)    #add number error type 
    writer.writerow(["Error", "Count"])
    for key, value in sorted_error.items():
        writer.writerow([key, value])  

        
