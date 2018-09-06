# Extraction

This repository has many uses. As such, the content is broken down into 3 folders:


### 1) FuelSensitivity

Purpose: sensitivity.py takes compounds that have RON and MON and find the fuel sensivity
of the compounds (RON - MON = Fuel Sensitivity). 

Important Notes:

•   The final results which are the compound names and fuel sensitivity 
    numbers are in lastnames.txt and Sensitivity.txt, respectively.

•   The folder contains the single program sensitivity.py which inputs compound names 
    with RON and MON values from RON.txt and MON.txt, respectively.

•   Running sensitivity.py generates the text files MON-in-RON.txt, RON-from-MON.txt, 
    lastnames.txt, and Sensitivity.txt.

•   There might be some errors due to the tab spacing of text files. If these errors
    arise, use a text editor to fix the tab spaces. 


### 2) Screening

Purposes: (1) finding the difference in compounds between two files; (2) extracting data 
from a local HTML/XML file; (3) finding the PubChem IDs of compounds from their names. 

More about each purpose:

(1): compcheck.py inputs two files olist.txt and test.txt which are located in the folder
     checkcomptext. The file olist.txt should contain the (original) list of compound 
     names, while test.txt is the (new) list of compounds names for which we want to check 
     which compounds if any are not found in the original olist.txt of compounds. 

     If there are any new compounds found, then the names are written to the newly 
     generated file newcomp.txt. 

(2): extract.py opens a specified local XML (can easily be changed to accomodate HTML) file
     and extracts compounds from the file that contain PubChem and/or CAS ID numbers.

(3): pcid.py takes in compound names from names.txt and retrieves their respective PubChem
     IDs. The results are printed to the console. 


### 3) Visualization

Purposes: (1) testing the graphing capabilities; (2) generating the graphs for RON, MON, and
Surface Tension of Pure Fuels with the median values included; (3) generating the graphs 
depicting the total amounts of data gathered; (4) generating the Venn diagram for the data 
also used from purpose (2) to find compounds that contain ideal values for RON, MON, and 
Surface Tension. 

More about each purpose:

(1): graphs.py is a test run of using matplotlib

(2): metagraph.py creates the graphs illustrating the values of RON, MON, and Surface Tension
     gathered and also show the median values as a dotted red line. The input is directly 
     pasted into metagraph.py, however, this can be changed to take in values from a text file
     instead. Also, each graph section is commented out, however feel free to uncomment any 
     section when needed for generating the respective graph. 

(3): totals.py creates the graphs depicting the total amount of data gathered. There are two 
     sections, one for the total amount of compound data gathered, and another for the total 
     amount of new compound data gathered (new compounds found). Again, one section is 
     commented out and can be uncommented when needed for the respective graph. 

(4): venn_diagram.py creates a colorful Venn diagram depicting molecules with high RON, high
     MON, and low Surface Tension. The diagram currently uses the data being used in 
     metagraph.py because the two programs were used in creating the BioCompoundML poster for
     the Posters on the Patio event. 
