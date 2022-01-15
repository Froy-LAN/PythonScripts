#!/usr/bin/env python3
import re
import operator
import csv
from collections import OrderedDict

error = {}
per_user = {}
log = []

with open('syslog.log') as f:
    log = f.readlines()

for line in log:
    log[log.index(line)] = line.strip()


pattern_err = r"ticky: ERROR ([\w \']*) \(([\w.]*)\)"
pattern_inf = r"ticky: INFO ([a-zA-Z ]*) \[#\d*\] \((\w.*)\)"

for line in log:
    if re.search(pattern_err, line):

        x = re.search(pattern_err, line)

        if x.group(1) not in error:
            error[x.group(1)] = 1
        else:
            error[x.group(1)] += 1

        if x.group(2) not in per_user:
            per_user[x.group(2)] = [0, 1]
        else:
            per_user[x.group(2)] = [per_user.get(x.group(2))[0], per_user.get(x.group(2))[1] + 1]

    elif re.search(pattern_inf, line):

        y = re.search(pattern_inf, line)

        if y.group(2) not in per_user:
            per_user[y.group(2)] = [1, 0]
        else:
            per_user[y.group(2)] = [per_user.get(y.group(2))[0] + 1, per_user.get(y.group(2))[1]]


sorted_error = OrderedDict()
sorted_user = OrderedDict()

for item in (sorted(per_user.items(), key=operator.itemgetter(0))):
    sorted_user[item[0]] = item[1]

for item in (sorted(error.items(), key=operator.itemgetter(1), reverse=True)):
    sorted_error[item[0]] = item[1]


with open('user_statistics.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "INFO", "ERROR"])
    for key, value in sorted_user.items():
        writer.writerow([key, value[0], value[1]])

with open('error_message.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Error", "Count"])
    for key, value in sorted_error.items():
        writer.writerow([key, value])
