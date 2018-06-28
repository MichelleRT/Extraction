"""

This program will extract data from a local HTML/XML file. 

"""

from bs4 import BeautifulSoup
import urllib2
import urllib 

page = urllib.urlopen("file:///Users/mtse/Documents/metacyc_data/metabolic-reactions.xml")
soup = BeautifulSoup(page, "html.parser")

print(soup)
