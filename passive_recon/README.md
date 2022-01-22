The 'scraping.py' script scrapes registered subdomain names from Certificate Transparency (CT) logs found in https://crt.sh; the website includes a simple search bar
to enter a domain name, which will then yield any linked subdomains. The files 'subdomains.txt' and 'example.com' are included to show what the script should yield, 
but these can be deleted since executing the script will create them again. 

To request the information for a particular domain, the it is possible to use an HTTP request with the following syntax:
https://crt.sh/q=domain_name

Using the requests module, an HTTP request is made to store the page content then write it in bytes to the file 'example.txt' so that it is not necessary
to constantly make requests if the scrip is executed multiple times. The script reads the information from the same file and facilitates extracting the information after
using BeautifuSoup's html.parser. 

The subdomains are listed within the 5th column in the third table. To extract this, the script first assigns all entries with a <td> tag to a list, which are individual entries
for slot in the table. Then, a second list is assigned only every 7th entry beginning from the 5th spot to excluse unwante information. Lastly, these subdomains are both printed
and writtedn to a file called 'subdomains.txt.
  
Potential improvements: request user to input a domain name to change the results. 
