#!/usr/bin/env python3
import re
import operator
import csv
from collections import OrderedDict #used instead of a dictionary as it is not ordered in some versions of Pytho

error = {}          #dictionary to retain error messages and the number of each
per_user = {}       #dictionary to contain how many INFO or ERROR log entries there are per user
log = []            #list to inster lines from log into

with open('syslog.log') as f:    #read lines from log
    log = f.readlines()

for line in log:                 #get rid of any space at either end of each line
    log[log.index(line)] = line.strip()


pattern_err = r"ticky: ERROR ([\w \']*) \(([\w.]*)\)"
pattern_inf = r"ticky: INFO ([a-zA-Z ]*) \[#\d*\] \((\w.*)\)"

for line in log:                        #used to distinguish ERROR vs INFO entries on the log
    if re.search(pattern_err, line):

        x = re.search(pattern_err, line)          #if it is an ERROR entry, add the message to the corresponding dictionary
                                                  
        if x.group(1) not in error:
            error[x.group(1)] = 1
        else:
            error[x.group(1)] += 1

        if x.group(2) not in per_user:           #increase the number of ERROR entires per user 
            per_user[x.group(2)] = [0, 1]
        else:
            per_user[x.group(2)] = [per_user.get(x.group(2))[0], per_user.get(x.group(2))[1] + 1]

    elif re.search(pattern_inf, line):          #if it is an INFO entry, do not add the message to the ERROR dictionary

        y = re.search(pattern_inf, line)

        if y.group(2) not in per_user:          #increase the number of INFO entries per user
            per_user[y.group(2)] = [1, 0]
        else:
            per_user[y.group(2)] = [per_user.get(y.group(2))[0] + 1, per_user.get(y.group(2))[1]]


sorted_error = OrderedDict()             #create orderd dictionary objects 
sorted_user = OrderedDict()

for item in (sorted(per_user.items(), key=operator.itemgetter(0))):       #move objects from unordered dictionaries to ordered ones
    sorted_user[item[0]] = item[1]

for item in (sorted(error.items(), key=operator.itemgetter(1), reverse=True)):
    sorted_error[item[0]] = item[1]


with open('user_statistics.csv', 'w') as file:                        #create csv files to hold the processed log information as stored 
    writer = csv.writer(file)                                         #in the ordered dictionaries
    writer.writerow(["Username", "INFO", "ERROR"])
    for key, value in sorted_user.items():
        writer.writerow([key, value[0], value[1]])

with open('error_message.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Error", "Count"])
    for key, value in sorted_error.items():
        writer.writerow([key, value])
