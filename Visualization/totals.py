"""

This program generates the bar graphs for the compound total lists
(MON, RON, TSI, Type, CN). There are two bar graphs created:

(1) Bar graph displaying the amount of total numbers gathered as 
    opposed to the original amount of numbers given. 

(2) Bar graph displaying the amount of new compounds gathered as 
    opposed to the original amount of compounds given. 

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.spines as spines 


"Get rid of the top and right spines and ticks" 

ax = plt.subplot(111) # main axes is subplot(111) by default 
### Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

### Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom') 



"(1) Make the bar graph for total amount of numbers gathered"

# ### Numbers for the original and new bars 
# originaldata = (188, 0, 323, 98, 0) 
# newdata = (748, 665, 853, 70, 328)  

# ### Locations of x tick marks and width of bars
# xticklocations = np.arange(5)   
# width = 0.4       

# ### Make the bar graphs
# p1 = plt.bar(xticklocations, originaldata, width, align='center', color='pink')
# p2 = plt.bar(xticklocations, newdata, width, bottom=originaldata, align='center', color='green')   

# ### Make the labels/title
# plt.ylabel('Amount of Compound Data Found\n')
# # plt.xlabel('Category') 
# plt.title(r'$\mathrm{Total\ New\ Numerical\ Data\ vs\ Original\ Data}$', fontsize=20) 
# # plt.title('New Data vs Original Data', fontsize=20)
# plt.xticks(xticklocations, ('RON', 'MON', 'CN', 'TSI', 'Sensitivity'))
# plt.yticks(np.arange(0, 1300, 100))
# plt.legend((p1[0], p2[0]), ('Original Data', 'Total New Data'))

# ### Display/Save the graph
# # plt.show() 
# plt.savefig('/Users/mtse/Documents/SensitivityTotals/TotalNumerical.eps', format='eps', dpi=1000) 



"(2) Make the bar graph for total amount of new compounds gathered"

### Numbers for the original and new bars 
originaldata = (188, 0, 323, 98, 0) 
newdata = (256, 348, 504, 70, 328)   

### Locations of x tick marks and width of bars
xticklocations = np.arange(5)   
width = 0.4       

### Make the bar graphs
p1 = plt.bar(xticklocations, originaldata, width, align='center', color='pink')
p2 = plt.bar(xticklocations, newdata, width, bottom=originaldata, align='center', color='green')   

### Make the labels/title
plt.ylabel('Amount of Compound Data Found\n')
# plt.xlabel('Category') 
plt.title(r'$\mathrm{Unique\ New\ Numerical\ Data\ vs\ Original\ Data}$', fontsize=20) 
# plt.title('New Data vs Original Data', fontsize=20)
plt.xticks(xticklocations, ('RON', 'MON', 'CN', 'TSI', 'Sensitivity'))
plt.yticks(np.arange(0, 1000, 100))
plt.legend((p1[0], p2[0]), ('Original Data', 'Unique New Data')) 

### Display/Save the graph
# plt.show() 
plt.savefig('/Users/mtse/Documents/SensitivityTotals/UniqueNumericalData.eps', format='eps', dpi=1000) 