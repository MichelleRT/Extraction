"""

This program will extract data from a local HTML/XML file. 

"""
# import codecs # for unicode encode
import io 
from bs4 import BeautifulSoup

page = open("/Users/mtse/Documents/metacyc_data/metabolic-reactions.xml", "r+")
soup = BeautifulSoup(page, "xml") 
tag = soup.species # If I just print soup.p it only prints the first <p>
type(tag)  


"open the files outside the loops, or else the file will be overwritten"
hi = io.open("#Name, PubChem.txt", encoding='utf-8', mode='a')
ha = io.open("#Name, CAS.txt", encoding='utf-8', mode='a') 

"We want to pull data for each species only if they contain CAS and/or PubChem"
for i in soup.findAll("species"): # sort through all the species
    for p in i.findAll("p"):
        if "PUBCHEM" in p.text:
            hi.write(i.get("name") + "    " + p.text[8:] + "\n") # we want to get rid of the letters and :
        if "CAS" in p.text:
            ha.write(i.get("name") + "    " + p.text[4:] + "\n") 
            
"Close the files after the iterations"
hi.close()
ha.close()   
     