This script analyzes the entries in the log 'syslog.log' by using regular expressions (regex) to extract information from it.

The log is composed of entries with the following structure: 
Month, Day of the Month, Time (Hour:Minute:Seconds), Host, 'ticky:', 'INFO'/'ERROR', Content Message, Ticket Number (only in INFO entries), Username

Here are a few examples:  
Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)  
Jan 31 00:16:25 ubuntu.local ticky: INFO Closed ticket [#1754] (noel)  
Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)  
Jan 31 00:44:34 ubuntu.local ticky: ERROR Permission denied while closing ticket (ac)  

The regular expression will be used to first decide if the entry is an ERROR or an INFO entry. 
If it is an INFO entry, a dictionary will keep the count of the total number of INFO entries per user, but the content message will not be used.
If it is an ERROR entry, a dictionary will keep count of the total number of ERROR entries per user, and an additional dictionary will keep count
of the total number of times each content message appears.

In case this is being executed in an environment where Python does not use ordered dictionaries by default, the contents of each dictionary
are transferred to an ordered dictionary object. The ordered dictionaries now hold the same values, except the one that keeps track of the number
of ERROR and INFO entries per user is organized alphabetically by username, and the one that keeps track of the frequency of each content message
for the ERROR entries is organized from the highest frequency to the lowest. 

At the end, the keys and values of the dictionaries are written to comma-seprated values (CSV) documents.
The documents may then be converted into html and viewed online or used for other purposes. 

Potential improvements: Recycle code by creating functions from code used to add information to dictionaries given the test conditions. 
