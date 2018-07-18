# we need to use sort/uniq to sort lines first
# lines_seen = set() # holds lines already seen 
lines_seen = set() 
outfile = open("/Users/mtse/Documents/Metabolic Reactions PubChem & CAS/#Name, PubChem copy.txt", "w+")
for line in open("/Users/mtse/Documents/Metabolic Reactions PubChem & CAS/#Name, PubChem copy.txt", "r+"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close() 