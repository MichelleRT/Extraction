import sys
import os
import io

"""

1) Open the files
2) Make a new file to write new compounds to
3) Check if the compounds in test.txt are in olist.txt
    --> If not in olist.txt, write the compound to the new text file
4) Close the files and use pcid.py for pubchem id's :) 

"""
olistfile = open("checkcomptext/olist.txt", "r")
testfile = open("checkcomptext/test.txt", "r")
newcompfile = open("checkcomptext/newcomp.txt", "a")

### Declare array for storing olistfile compounds
arr = []

"Store the compounds from olistfile into an array for comparison check"
for line in olistfile:
    comp = line.strip()
    arr.append(comp)

### If the compound in testfile is not in olistfile, add to newcompfile
for line in testfile:
    comp = line.strip() 
    if comp not in arr:
        newcompfile.write(comp + "\n")  

olistfile.close()
testfile.close()
newcompfile.close() 