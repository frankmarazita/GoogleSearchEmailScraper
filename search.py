from googlesearch import search
import requests
import re
import csv

NUM_GOOGLE_RESULTS = 10     # Number of google search results for each search
PAUSE = 0.5                 # Pause time in seconds between each google search
TIMEOUT = 5                 # Seconds before the request on the domain timeouts
DOMAIN_CONTAIN = '.com.au'  # String match in domain
INCLUDE_PDF = False  # If enabled, can take much longer (increase timeout)
SEARCH_KEYWORDS = " email contact vic"  # This will be appended to every search
ENABLE_CONSOLE = True

searches = []
with open('searches.txt') as f:
    searches = [line.rstrip('\n') for line in f]

with open('output.csv', mode='w', newline='') as file_output:
    file_writer = csv.writer(file_output, delimiter=',')

    for s in searches:
        if ENABLE_CONSOLE:
            print("Name:", s)
        file_writer.writerow(["Name: " + s])
        found = False
        try:
            domains = search(s + SEARCH_KEYWORDS, tld="com", num=NUM_GOOGLE_RESULTS, stop=NUM_GOOGLE_RESULTS, pause=PAUSE)
            for domain in domains:
                if not domain.endswith(".pdf") or INCLUDE_PDF:
                    if DOMAIN_CONTAIN in domain:
                        data = None
                        try:
                            data = requests.get(domain, timeout=TIMEOUT)
                        except:
                            if ENABLE_CONSOLE: print("Timeout")
                        emails = re.findall(
                            r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
                        emails_no_at = re.findall(
                            r'([\d\w\.]+%40[\d\w\.\-]+\.\w+)', data.text)
                        for other in emails_no_at:
                            emails.append(other.replace("%40", "@"))
                        # If no emails are found, skip
                        if len(emails) > 0:
                            file_writer.writerow([domain])
                            file_writer.writerow(emails)
                            if ENABLE_CONSOLE:
                                print(domain)
                                print(emails)
                            found = True
        except:
            pass
        if not found:
            file_writer.writerow(["NONE FOUND"])
        file_writer.writerow([])
        if ENABLE_CONSOLE:
            print("------------------------------------------------------------")
