# Google Search Email Scraper
A short python 3 script that finds emails on pages of google search results

### Installing Dependencies
* pip3 install -r requirements.txt

### Running The Application

1. Enter your search queries in 'searches.txt', each on a new line
2. Change parameters in the search.py file to better match your requirements
3. Run the code: python3 search.py

### Notes

* Keep in mind that if you are looking for specific results, there may be inconsistencies and/or false positives.
* Sites that use Cloudflare or similar protection may or may not express results.
* There is always the possibility of a temporary IP ban when conducting any form of web scraping.
    * The likelihood of this can be mitigated by increasing the pause parameter variable in the code.
* Using google search techniques found at https://support.google.com/websearch/answer/2466433?hl=en, can be helpful to use in the 'SEARCH_KEYWORDS' variable in order to better refine search results.