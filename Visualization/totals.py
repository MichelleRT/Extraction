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


"get rid of the top and right spines and ticks" 

ax = plt.subplot(111) # main axes is subplot(111) by default 
# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom') 


"Make the bar graph for total amount of numbers gathered"

# N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
# menStd = (2, 3, 4, 1, 2)
# womenStd = (3, 5, 2, 3, 3)
ind = np.arange(5)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

# p1 = plt.bar(ind, menMeans, width, yerr=menStd)
# p2 = plt.bar(ind, womenMeans, width,
#              bottom=menMeans, yerr=womenStd)
p1 = plt.bar(ind, menMeans, width, align='center', color='pink')
p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, align='center', color='white')   

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[1], p2[1]), ('Men', 'Women'))

plt.show() 


"Make the bar graph for total amount of new compounds gathered" 
