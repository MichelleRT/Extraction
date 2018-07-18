from pubchempy import get_compounds 
import io


"""

Currently using compounds from APIDATA, so we should iterate through compound names
and get the pubchem cids for each compound. :)

"""

# names = ["ETHANE","PROPANE","N-BUTANE","N-PENTANE","N-HEXANE","N-HEPTANE","N-OCTANE","ISOBUTANE","ISOPENTANE"]
# names = ["NEOPENTANE","2-METHYLPENTANE","3-METHYLPENTANE","2,2-DIMETHYLBUTANE","2,3-DIMETHYLBUTANE","2-METHYLHEXANE"]
# names = ["3-METHYLHEXANE","3-ETHYLPENTANE","2,2-DIMETHYLPENTANE","2,3-DIMETHYLPENTANE","2,4-DIMETHYLPENTANE"]
# names = ["3,3-DIMETMYLPENTANE"] "doesn't retrieve anything..."
# names = ["2,2,3-TRIMETHYLBUTANE","2-METHYLHEPTANE","3-METHYLHEPTANE","4-METHYLHEPTANE"]
# names = ["3-ETHYLHEXANE","2,2-DIMETHYLHEXANE","2,3-DIMETHYLHEXANE","2,4-DIMETHYLHEXANE","2,5-DIMETHYLHEXANE"]
# names = ["3,3-DIMETHYLHEXANE","3,4-DIMETHYLHEXANE","2-METHYL-3-ETHYLPENTANE","3-METHYL-3-ETHYLPENTANE","2,2,3-TRIMETHYLPENTANE"]
# names = ["2,2,4-TRIMETHYLPENTANE","2,3,3-TRIMETHYLPENTANE","2,3,4-TRIMETHYLPENTANE","2,2-DIMETHYLHEPTANE","3,3-DIETHYLPENTANE"]
# names = ["2,2-DIMETHYL-3-ETHYLPENTANE","2,4-DIMETHYL-3-ETHYLPENTANE","2,2,3,3-TETRAMETHYLPENTANE","3,3,5-TRIMETHYLHEPTANE"]
# names = ["2,2,3,3-TETRAMETHYLHEXANE","METHYLCYCLOPROPANE","ETHYLCYCLOPROPANE","CIS-1,2-DIMETHYLCYCLOPROPANE","ETHYLCYCLOBUTANE"] 
# names = ["CYCLOPENTANE","METHYLCYCLOPENTANE","ETHYLCYCLOPENTANE","1,1-DIMETHYLCYCLOPENTANE","CIS-1,3-DIMETHYLCYCLOPENTANE"]
# names = ["TRANS-1,3-DIMETHYLCYCLOPENTANE","N-PROPYLCYCLOPENTANE","ISOPROPYLCYCLOPENTANE","CIS-l-METHYL-3-ETHYL-CYCLOPENTANE"]
# names = ["TRANS-1-METHYL-3-ETHYL-CYCLOPENTANE"]
# names = ["1,1,3-TRIMETMYLCYCLOPENTANE"]
# names = ["l,CIS-2,TRANS-4-TRIMETMYL-CYCLOPENTANE"]
# names = ["N-BUTYLCYCLOPENTANE"]
# names = ["ISOBUTYLCYCLOPENTANE","CYCLOHEXANE","METHYLCYCLOHEXANE","ETHYLCYCLOHEXANE","1,1-DIMETHYLCYCLOHEXANE","CIS-1,2-DIMETHYLCYCLOHEXANE"]
# names = ["TRANS-1,2-DIMETHYLCYCLOHEXANE","CIS-I,3-DIMETMYLCYCLOHEXANE","TRANS-1,3-DIMETHYLCYCLOHEXANE","CIS-I,4-DIMETHYLCYCLOHEXANE"]
# names = ["TRANS-1,4-DIMETHYLCYCLOHEXANE","N-PROPYLCYCLOHEXANE"]
# names = ["ISOPROPYLCYCLOHEXANE","N-BUTYLCYCLOHEXANE","CYCLOHEPTANE","CYCLOOCTANE","ETHYLENE"]
# names = ["PROPYLENE","1-BUTENE","CIS-2-BUTENE","1-PENTENE","2-METHYL-1-BUTENE","2-METHYL-2-BUTENE","1-HEXENE","TRANS-2-HEXENE","TRANS-3-HEXENE"]
# names = ["2-METHYL-1-PENTENE","3-METHYL-1-PENTENE","4-METHYL-1-PENTENE","2-METHYL-2-PENTENE","TRANS-3-METHYL-2-PENTENE","CIS-4-METHYL-2-PENTENE"]
# names = ["TRANS-4-METHYL-2-PENTENE","2-ETHYL-1-BUTENE","2,3-DIMETHYL-1-BUTENE","3,3-DIMETHYL-1-BUTENE","2,3-DIMETHYL-2-BUTENE","1-HEPTENE","TRANS-2-HEPTENE"]
# names = ["CIS-3-HEPTENE"]
# names = ["TRANS-3-HEPTENE"]
# names = ["2-METHYL-1-HEXENE"]
# names = ["3-METHYL-1-HEXENE","4-METHYL-1-HEXENE","5-METHYL-1-HEXENE","2-METHYL-2-HEXENE"]
# names = ["CIS-3-METHYL-2-HEXENE"]
# names = ["TRANS-3-METHYL-2-HEXENE"]
# names = ["CIS-4-METHYL-2-HEXENE","TRANS-4-METHYL-2-HEXENE","TRANS-5-METHYL-2-HEXENE"]
# names = ["TRANS-2-METHYL-3-HEXENE","CIS-3-METHYL-3-HEXENE"]
# names = ["TRANS-3-METHYL-3-HEXENE"]
# names = ["3-ETHYL-1-PENTENE","3-ETHYL-2-PENTENE","2,3-DIMETHYL-1-PENTENE"]
# names = ["2,4-DIMETHYL-1-PENTENE","3,3-DIMETHYL-1-PENTENE","3,4-DIMETHYL-1-PENTENE","4,4-DIMETHYL-1-PENTENE","2,3-DIMETHYL-2-PENTENE","2,4-DIMETHYL-2-PENTENE"]
# names = ["CIS-3,4-DIMETHYL-2-PENTENE","CIS-4,4-DIMETHYL-2-PENTENE"]
# names = ["TRANS-4,4-DIMETHYL-2-PENTENE"]
# names = ["3-METHYL-2-ETHYL-1-BUTEME"]
# names = ["2,3,3-TRIMETHYL-1-BUTENE"]
# names = ["1-OCTENE"]
# names = ["TRANS-2-OCTENE"]
# names = ["TRANS-2-OCTENE"]
# names = ["TRANS-3-OCTENE"]
# names = ["TRANS-4-OCTENE"]
# names = ["2-METHYL-1-HEPTENE"]
# names = ["TRANS-6-METMYL-2-HEPTENE"]
# names = ["2,3-DIMETHYL-1-HEXENE"]
# names = ["2,3-DIMETHYL-2-HEXENE","CIS-2,2-DIMETHYL-3-HEXENE","2,3,3-TRIMETHYL-1-PENTENE","2,4,4-TRIMETHYL-1-PENTENE","2,4,4-TRIMETHYL-2-PENTENE"]
# names = ["3-METHYL-1,2-BUTADIENE","2-METHYL-1,3-BUTADIENE","1,5-HEXADIENE"]
# names = ["CYCLOPENTENE"]
# names = ["1-METHYL-CYCLOPENTENE"]
# names = ["1-ETHYLCYCLOPENTENE"]
# names = ["3-ETHYLCYCLOPENTENE"]
# names = ["CYCLOHEXENE","1-METHYLCYCLOHEXENE","1-ETHYLCYCLOHEXENE","DIMETHYLACETYLENE","1-OCTYNE","BENZENE","TOLUENE","ETHYLBENZENE","O-XYLENE","M-XYLENE"]
# names = ["P-XYLENE","N-PROPYLBENZENE","ISOPROPYLBENZENE","O-ETHYLTOLUENE","M-ETHYLTOLUENE","P-ETHYLTOLUENE","1,2,3-TRIMETHYLBENZENE","1,2,4-TRIMETHYLBENZENE"]
# names = ["1,3,5-TRIMETHYLBENZENE","N-BUTYLBENZENE","ISOBUTYLBENZENE","SEC-BUTYLBENZENE","TERT-BUTYLBENZENE","1-METHYL-2-N-PROPYLBENZENE"] 
# names = ["1-METHYL-3-N-PROPYLBENZENE","O-CYMENE"]
# names = ["P-CYNENE"]
# names = ["M-DIETHYLBENZENE"]
# names = ["P-DIETHYLBENZENE","1,2-DIMETHYL-3-ETHYLBENZENE","1,3-DIMETHYL-4-ETHYLBENZENE"]
# names = ["1,3-DIMETHYL-5-ETHYLBENZENE","1,4-DIMETHYL-2-ETHYLBENZENE","1,2,3,4-TETRAMETHYLBENZENE","1,2,3,5-TETRAMETHYLBENZENE","STYRENE"]
# names = ["CIS-l-PROPENYL BENZENE"]
# names = ["TRANS-l-PROPENYL BENZENE"]
# names = ["2-PROPENYL BENZENE"]
names = ["1,2,3,4-TETRAHYDRONAPHTHALENE","INDENE","2,3-DIHYDROINDENE"]



# chemType = ["Normal paraffin","Normal paraffin","Normal paraffin","Normal paraffin","Normal paraffin","Normal paraffin","Normal paraffin,Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Paraffin (non-normal)","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Naphthene - major structure is saturated ring","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Olefin (alkene) with single C=C double bond","Diolefin - has two C=C double bonds","Diolefin - has two C=C double bonds","Diolefin - has two C=C double bonds","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Cyclic olefin with a single C=C double bond within the otherwise saturated ring","Alkene with triple bond between carbons","Alkene with triple bond between carbons","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring)","Aromatic (single ring) with attached olefin side chain","Aromatic (single ring) with attached olefin side chain","Aromatic (single ring) with attached olefin side chain","Aromatic (single ring) with attached olefin side chain","Aromatic with attached saturated rings","Aromatic with attached unsaturated (but not aromatic) rings","Aromatic with attached saturated rings"] 
# fileP = io.open("MorePubChem.txt", encoding='utf-8', mode='a') 

for name in names: # iterate through the names 
    "We want to get the pubchem cids of each compound"
    for compound in get_compounds(name,'name'):
        print(compound.cid) # this is the pubchem cid for each compound 
        # fileP.write(pid)  

# fileP.close()  


