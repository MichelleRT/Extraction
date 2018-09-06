from pubchempy import get_compounds 
import io


"""

This program will take the compounds listed in names.txt (see example), then
gather the PubChem IDs for each compound and print them to the console.

Please note the current format prints the name of the compound, then its 
respective PubChem ID (there may be more than one ID number found). 

However, the user can choose to change the output format to what is more
useful/needed. 

"""
counter = 0

fileObject = io.open("names.txt", encoding='utf-8', mode='r+') 
newfile = open("pubchemids.txt",'a') 
# print(fileObject.readlines()) 
totaltext = fileObject.readlines()
for name in totaltext:
    counter += 1
    # print(counter) 
    # print(name) 
    for compound in get_compounds(name, 'name'):
        print name, compound.cid, "\n" 
        # print compound.cid 
    
newfile.close() 
fileObject.close()