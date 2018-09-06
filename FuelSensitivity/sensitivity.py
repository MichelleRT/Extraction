"""

This program finds the compounds that are in both the MON and RON files, 
then extracts the compounds and the MON and RON values to find the fuel
sensitivity (RON - MON). 

Please note that there might be errors due to the tab spacing of the 
text file, so you may want to check the tab spacing of the text file(s)
on a text editor if there are errrors. 



FINAL RESULTS:

The final results should be in lastnames.txt and Sensitivity.txt for the 
fuel sensitivity compound names and fuel sensitivity numbers, respectively.
The names and numbers are in separate text files to avoid tab spacing
errors and to provid the names and numbers in different files for easier 
management of the data. 

"""

import sys
import os
import io


monfile = open("MON.txt","r")
ronfile = open("RON.txt","r") 
mrfile = open("MON-in-RON.txt","a") 
Rfile = open("RON-from-MON.txt","a") 
sfile = open("Sensitivity.txt","a")



"Method for retrieving the columns of data from a text file"

def getDataColumns(inputFile, delim="\t", header=True):
    ### Make the dictionaries for columns and indices to columns
    columns = {}
    indexToCol = {}
    ### Go through the lines of the text file
    for lineNum, line in enumerate(inputFile):
        ### The header should be the very first line (hence at index 0) 
        ### Other lines should not be headers
        if lineNum == 0:
            headings = line.split(delim)
            i = 0
            for heading in headings:
                heading = heading.strip()
                columns[heading] = []
                indexToCol[i] = heading
                i += 1
        else:
            cells = line.split(delim)
            i = 0
            for cell in cells:
                cell = cell.strip()
                columns[indexToCol[i]] += [cell] 
                i += 1          
    return columns, indexToCol


"Store the name and mon value"

cols, ind = getDataColumns(monfile)
nameCol = cols['#Name']
numCol = cols['MON']
### Keep track of the name index & number index for mon
mi = 0
mj = 0
### Store the mon names & numbers
monNames = [] 
monNums = []
for name in nameCol:
    mi += 1
    monNames.append(name)
for num in numCol:
    mj += 1
    monNums.append(num) 


"Store the name and ron value"

rcols, rind = getDataColumns(ronfile)
rnameCol = rcols['#Name']
rnumCol = rcols['RON']
### Keep track of the name and number index for ron
ri = 0
rj = 0
### Store the ron names and numbers
ronNames = []
ronNums = []
for name in rnameCol:
    ri += 1
    ronNames.append(name)
for num in rnumCol:
    rj += 1
    ronNums.append(num) 


"""

Sort through the MON compounds and if there is a match in the 
RON list, then store the MON compound name and MON number in 
the mrfile. 

"""
i = 0
# ### put in the header, then append names & values
# mrfile.write("#Name" + "    " +  "Data" + "\n") 
# for comp in monNames:
#     if comp in ronNames:
#         mrfile.write(comp + '    ')  
#         mrfile.write(monNums[i] + '\n')
#     i += 1 


"""

Iterate through the compounds in the mrfile to find the 
respective RON number. Put the RON numbers into the Rfile. 

"""

mrfile = open("MON-in-RON.txt","r+") 

c, indi = getDataColumns(mrfile)
mrnameCol = c['#Name']
mrnumCol = c['Data'] 

"Writing the RON values to Rfile"
# y = 0
# for name in mrnameCol:
#     if name in ronNames:
#         Rfile.write(ronNums[y] + '\n') 
#     y += 1


"""

Now we do RON-MON = Sensitivity and store the results in the 
Sensitivity.txt (sfile). 

"""

# Rfile = open("RON-from-MON.txt","r+")

# t = 0
# length = len(mrnumCol)

# if t < length:
#     for ron in Rfile:
#         a = float(ron)
#         mon = mrnumCol[t]
#         b = float(mon) 
#         sens = a-b
#         sfile.write(str(sens) + '\n') 
#     t += 1

"""

Write the list of compounds for fuel sensitivity to a 
separate text file lastnames.txt (lastnamefile) to avoid 
tab spacing errors.

"""

lastnamefile = open("lastnames.txt","a")

for compound in mrnameCol:
    lastnamefile.write(compound + '\n') 

          

lastnamefile.close()
monfile.close()
ronfile.close()
mrfile.close() 
Rfile.close() 
sfile.close() 