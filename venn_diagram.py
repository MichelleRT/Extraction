from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn3, venn3_circles

plt.figure(figsize=(4,4))
v = venn3(subsets=(143, 54, 53, 144, 61, 35, 34), set_labels = ('RON', 'MON', 'Surface Tension')) 
for text in v.subset_labels: # Make the numbers inside the circles bold! 
    text.set_weight('bold') 


# c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), linestyle='dashed')

plt.title("RON, MON, Surface Tension Count")  

# plt.show() 
plt.savefig('/Users/mtse/Documents/VennDiagram.eps', format='eps', dpi=1000) 