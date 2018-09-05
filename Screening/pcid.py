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

# print(fileObject.readlines()) 
totaltext = fileObject.readlines()
for name in totaltext:
    counter += 1
    # print(counter) 
    # print(name) 
    for compound in get_compounds(name, 'name'):
        print name, compound.cid, "\n" 
    
        # if compound.cid != None:
        #     # print(compound.cid)
        #     print("yes")   
        # elif compound.cid == None: 
        #     # print(name + " " + "has no found pubchem id")
        #     print("none found, sorry :((((") 

fileObject.close()

# names = ["2-Methyl propane","4,4-Dimethyl-1-heptene"] 

# chemType = ["Normal paraffin","Normal paraffin","Normal paraffin","Normal paraffin","Normal paraffin","Normal paraffin","Normal paraffin,Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Diolefin - has two C=C double bonds","Diolefin - has two C=C double bonds","Diolefin - has two C=C double bonds","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Alkene with triple bond between carbons","Alkene with triple bond between carbons","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring) with attached olefin side chain","Aromatic (single ring) with attached olefin side chain","Aromatic (single ring) with attached olefin side chain","Aromatic (single ring) with attached olefin side chain","Aromatic with attached saturated rings","Aromatic with attached unsaturated (but not aromatic) rings","Aromatic with attached saturated rings"] 
# fileP = io.open("MorePubChem.txt", encoding='utf-8', mode='a') 

# for name in names: # iterate through the names 
#     "We want to get the pubchem cids of each compound"
#     for compound in get_compounds(name,'name'):
#         print(compound.cid) # this is the pubchem cid for each compound 
#         # fileP.write(pid)  

# fileP.close()  


