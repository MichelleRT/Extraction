"""
We need to make graphs for RON and the other fuel properties
(see the graph on page 3/9 of the BioCompoundML paper for
reference). We will be using matplotlib to create bar graphs. 

"""

"""

This section is for Pure Surface Tension

"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
# import seaborn as sns 
import matplotlib.spines as spines 


x = [23.9,28.2,31.4,40.7,40.1,51.1,28.3,22.56,37,31.2,26.5,20,22.9,33.5,52.1,25.6,25.6,25.6,26,22,23,28,38.7,28.5,27.4,25.7,32.1,25.5,25.5,25.7,22.7,18.9,16.41,16.8,35.3,25.3,24.3,23.6,21.9,26.6,24,20.6,25.3,26.4,20.7,22.8,25.7,24.7,27.4,25.2,37.3,23,23,37.8,40.6,37.6,26.5,50,33.1,35.2,30.5,26.4,29.7,36.9,28.22,28.8,28.8,29.5,19.4,20.2,44.6,34.9,27.1,27,31.6,40.1,29.7,57.2,23.3,23.3,49.4,24.98,33.47,28.9,26.4,34,23.92,23,17.06,26.6,22.4,16,25.6,21.1,19.8,29.6,30.7,30.1,30.4,25.7,43.4,30.93,25.2,26,24.8,38.9,40.7,38,29.4,25.9,31.5,27.6,20.7,21,38,47.5,57.2,30.81,16.9,39.6,31.2,32,23.97,29.7,31.3,24.73,23.9,19.7,23.6,19.2,23,24.93,22.38,23.6,32.5,23.75,26.5,25,27.9,21.14,22.9,26.9,25.5,16,32.8,44.1,39.7,25.5,25.3,16,26.5,16.7,38.8,57.2,37.2,26.8,26.8,28.93,51.8,26.1,47.3,35,21.8,29.2,28.5,29.3,25.3,25.3,26.17,26.5,25.4,26.7,24,23.94,27.3,28.3,28.3,29.1,26,23.3,27.3,27.6,21.9,21.9,27.4,20.6,19.66,23,27.3,29.76,29.71,21.6,28.09,26.5,25.3,27.1,26.85,28.5,39,27,27.53,25.4,25.7,26.2,27.4,34.6,28.6,34.4,32.5,31.9,28.7,36.1,24.7,24.7,14.5,25.6,31.2,24.9,24.8,31,22.8,23.9,26.5,26.5,30.1,24.9,31.3,29.3,29.1,29.6,28,23.37,27.3,31.6,22.77,22.4,24.77,24.9,27,27.69,22.1,23.4,24.4,26.2,25,26,20.93,21.97,20.7,25,27.7,23.7,26,21.9,29.2,33.3,25.8,24.7,23.6,23.9,24.8,25.6,27.4,35.05,26.2,21.4,22.8,23.9,23.9,27.4,25.73,26.6,25,23.9,22.6,29.2,23.1,22.4,24.3,28.84,25.9,23.7,22.07,37.3,37.3,21.1,23.5,28.8,30.7,26.9,38.6,31.7,30.6,29.4,28.7,32.6,24.3,25,28.2,30.8,31.93,22.3,24,24,28.3,25.6]

# the histogram of the data
n, bins, patches = plt.hist(x, 20, facecolor='green', alpha=0.5)

plt.xlabel('Observed Surface Tension')
plt.ylabel('Count')
plt.title(r'$\mathrm{Surface\ Tension\ of\ Pure\ Fuels}$') 
plt.axis([0, 60, 0, 70]) # (x origin, x endpoint, y origin, y endpoint)
# plt.grid(True)
plt.grid(False) 

"get rid of the top and right spines" 
ax = plt.subplot(111) # main axes is subplot(111) by default 
# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom') 

"get the median of the data"
med = np.median(x) 
print(med) 

"plot the median as a red line and label the line"
plt.axvline(med, color='red', linestyle='dashed', linewidth=1, label='median')
plt.legend(loc='upper right', title='Legend') # creates the legend box
# plt.legend(loc='upper left') 

# plt.show() # messes up the plt.savefig to empty

# plt.savefig('/Users/mtse/Documents/Pure_Surface_Tension.eps', format='eps', dpi=1000) 


"""

This section is for Pure RON using the total list (new + old RON data)

"""

# import numpy as np
# import matplotlib.mlab as mlab
# import matplotlib.pyplot as plt

# x = [120,120,118,115.4,111,110.5,110.3,109,109,107.2,107,107,106.6,106.5,105.7,105.3,105,104,104,103.3,103,103,102.9,102.7,102.1,102,101.3,101,100.8,100.6,100,100,100,99.5,99.4,98,98.8,57.6,54.5,76.4,67.3,68.7,57.6,29.9,28.7,87.9,87.3,92.3,95.7,96.2,81.3,81.7,80.9,84.8,89.2,72.9,89.2,69.3,79.9,63.8,67.7,101.6,99.3,97,73.4,92.7,98.3,70.2,90.7,94.2,97.3,79.8,97.8,87.3,94.6,97.9,92.3,21.7,42.4,73.4,106.3,56.3,87.8,112.1,106,91.8,50.3,72.5,92.8,85.5,112.1,109.6,112.8,116.8,100,101.3,96.3,99.3,97.4,93.1,97.5,104.3,71.3,91.1,106,106.1,96.6,102.7,99.2,100,105.3,65.2,83.1,106,103.5,95.2,101.9,55.2,95.6,99.5,95.6,93.7,84,33.5,65,90,94,97.5,82.2,96,97.2,80.8,96.2,26.8,52,74.5,72.5,111.7,103.5,75.5,86.4,86.4,96.2,103,86.4,95.7,98.9,26.7,73.3,79.8,104.4,105.3,75.5,63.8,71.3,91.3,94,38.9,84,71,101.6,114.9,97.3,28,46.5,67.2,0,24.8,33.7,33.4,62.8,81.1,93,73.8,89.3,102.1,31,17.8,31.2,0,67.3,61.8,111,101.8,17.8,31.2,51,98.5,8.8,89.4,35,-123.5,92,102,44.2,36,83.2,102,86,90,-19.2,-15.6,94.1,101.9,93.5,-1,103,88,86.6,64.8,73,120,112,104.5,63.8,72,74.5,83.9,96.4,-24,-85,119,-53.3,-17.5,67,82.3,109,53,102,100,42,65.2,99,120.3,105.7,110,82.5,-34,82,80,87.9,87.9,120,103.5,74.7,69,36.8,87.3,118,115.4,76.5,69.4,72.4,45.6,87.1,108.9,97,74.6,108.6,110,77,73.5,103.9,48.5,97.2,98.4,99.2,100.5,70,109.7,112.3,10,60,85.5,85,102.9,104,-41,60,111,98.8,113,87.1,108.7,79.6,91.7,101,69.3,98.5,120,103.4,109,107.5,97.1]

# # the histogram of the data
# n, bins, patches = plt.hist(x, 20, facecolor='green', alpha=0.5)

# plt.xlabel('Observed RON')
# plt.ylabel('Count')
# plt.title(r'$\mathrm{RON\ of\ Pure\ Fuels}$') 
# plt.axis([-150, 150, 0, 100]) # (x origin, x endpoint, y origin, y endpoint)

# plt.grid(False)

# "get rid of the top and right spines" 
# ax = plt.subplot(111) # main axes is subplot(111) by default 
# # Hide the right and top spines
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)

# # Only show ticks on the left and bottom spines
# ax.yaxis.set_ticks_position('left')
# ax.xaxis.set_ticks_position('bottom') 

# "get the median of the data"
# med = np.median(x) 
# print(med) 

# "plot the median as a red line and label the line"
# plt.axvline(med, color='red', linestyle='dashed', linewidth=1, label='median')
# plt.legend(loc='upper left', title='Legend') # creates the legend box
# # plt.legend(loc='upper left') 

# # plt.show() # messes up the plt.savefig to empty

# # plt.savefig('/Users/mtse/Documents/Pure_RON.eps', format='eps', dpi=1000)


"""

This section is for Pure MON

"""

# import numpy as np
# import matplotlib.mlab as mlab
# import matplotlib.pyplot as plt

# x = [-16.7,85,92.5,16.5,88.1,93,87.9,86.1,73,90.8,103.4,77.2,-82.7,-44.4,78,80,74,56,-6.2,90.8,99.9,89.1,50.5,74,115,101,103.5,77,73.4,89,103,41,91.6,100,46,69.8,105.5,120.3,71,105.5,76.6,85,89,76,62,57.3,14,82.9,82.9,104,90.5,35,92,78.1,84,120.3,106.2,74.7,86.8,90.7,70.5,69,100,0,90,100,104.4,80,98,65,55.8,59,91.2,109.5,99.1,100.2,97.2,105.2,60,78.1,75.6,91,97,99,94,-38,86.8,99,82,96.7,90,87,95,112.3,120,60.5,104.7,102.2,64.1,85,88.8,120,101.1,120,89,108.1,88.3]

# # the histogram of the data
# n, bins, patches = plt.hist(x, 20, facecolor='green', alpha=0.5)

# plt.xlabel('Observed MON')
# plt.ylabel('Count')
# plt.title(r'$\mathrm{MON\ of\ Pure\ Fuels}$') 
# plt.axis([-100, 150, 0, 30]) # (x origin, x endpoint, y origin, y endpoint)

# plt.grid(False)

# "get rid of the top and right spines" 
# ax = plt.subplot(111) # main axes is subplot(111) by default 
# # Hide the right and top spines
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)

# # Only show ticks on the left and bottom spines
# ax.yaxis.set_ticks_position('left')
# ax.xaxis.set_ticks_position('bottom') 

# "get the median of the data"
# med = np.median(x) 
# print(med) 

# "plot the median as a red line and label the line"
# plt.axvline(med, color='red', linestyle='dashed', linewidth=1, label='median')
# plt.legend(loc='upper left', title='Legend') # creates the legend box
# # plt.legend(loc='upper left') 

# # plt.show() # messes up the plt.savefig to empty

# # plt.savefig('/Users/mtse/Documents/Pure_MON.eps', format='eps', dpi=1000)


"""

This section is for Pure Sensitivity

"""

# import numpy as np
# import matplotlib.mlab as mlab
# import matplotlib.pyplot as plt

# x = [25.5,89.4,76,35,-123.5,92,102,15,6.5,27.7,13.2,36,14,83.2,14.1,16.9,13,8.6,2.3,12.8,63.5,28.8,12,94.1,101.9,14,19.5,-4,5.2,12.2,6.9,88,-2.5,14.3,-1,5,11,1,63.8,72,74.5,6,10.5,12,96.4,-24,-85,16,-53.3,26,-17.5,67,82.3,17.4,53,102,0,-4,-4.6,99,5.5,0,3.1,0.2,110,5.9,13,-34,-18,6,0,101.7,22.7,4,5,5,16,12.8,-8,11.5,74.7,-9.1,36.8,3.3,-2.3,9.2,1.8,69.4,72.4,45.6,87.1,22.1,6.3,2,4,74.6,0,0,15,20,4.2,11,12,12,17.7,21.9,103.9,48.5,102,97.2,98.4,8,100.5,70,109.7,0.8,13.2,0.9,3.4,2,810.1,10,0,7.4,9.4,11.9,10,12,10,-3,60,111,12,14,-1,87.1,15.8,19,19,7.7,-3.6,-120,19.1,-1.1,91.7,101,6.7,5.2,5.8,9.7,0,2.3,-120,20,-0.6,8.8]

# # the histogram of the data
# n, bins, patches = plt.hist(x, 100, facecolor='green', alpha=0.5)

# plt.xlabel('Observed Sensitivity')
# plt.ylabel('Count')
# plt.title(r'$\mathrm{Sensitivity\ of\ Pure\ Fuels}$') 
# plt.axis([-150, 150, 0, 50]) # (x origin, x endpoint, y origin, y endpoint)

# plt.grid(False)

# "get rid of the top and right spines" 
# ax = plt.subplot(111) # main axes is subplot(111) by default 
# # Hide the right and top spines
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)

# # Only show ticks on the left and bottom spines
# ax.yaxis.set_ticks_position('left')
# ax.xaxis.set_ticks_position('bottom') 

# "get the median of the data"
# med = np.median(x) 
# # print(med) 

# "plot the median as a red line and label the line"
# plt.axvline(med, color='red', linestyle='dashed', linewidth=1, label='median')
# plt.legend(loc='upper left', title='Legend') # creates the legend box
# # plt.legend(loc='upper left') 

# # plt.show() # messes up the plt.savefig to empty

# plt.savefig('/Users/mtse/Documents/Pure_Sensitivity.eps', format='eps', dpi=1000)




"""

This section is for Blend RON

"""

# import numpy as np
# import matplotlib.mlab as mlab
# import matplotlib.pyplot as plt

# x = [108,99.4,102,90.3,91.6,93.2,94.8,93.1,96.1,98.2,91.1,92.8,93.9,89.5,91.5,93.3,90.7,91.9,93.1,98.1,100.8,101.6,91.1,92.5,93.4,92.9,95.5,97.2,92.1,95.3,98.5,91.9,96.8,99.2,94.1,97.6,100.3,92.5,95.4,98.5,96.2,100.4,102,96.4,100.9,102.6,92.6,95.7,98.4,94.1,97.9,100.1,96.9,99.8,106,97.4,93.7,97.3,100.5,98.1,101.4,102,92.7,89.7,89.5,93.3,92.5,96.2,95.1,92.2,90.6,89,90.2,97,93.7,92.6,93.8,99.9,97.7,96,97.3,100,98.3,101,92.7,95,97.5,94,96.7,97.4,90.6,94.2,97.6,90.9,94.4,96.6,90,92.6,95.3,90.4,93.7,96.6,90.1,93,96,93.4,96.8,98.4,92.5,96.9,98.7,88.9,89.6,96,100.4,101.1,100.6,101,100.5,101.1,101.1,101.3,101,101.1,101.2,101.1,96.4,92,93.1,94.4,92.5,95,98.3,90.7,91.7,92.9,96.4,96.9,97.8,98,96.6,99.6,97.8,96.4,96.8,97.4,98.5,92.6,95.8,98.3,94.1,94.5,98,100.5,92.7,96.9,99.8,88.5,88.8,91.8,96.5]

# # the histogram of the data
# n, bins, patches = plt.hist(x, 20, facecolor='green', alpha=0.5)

# plt.xlabel('Observed RON')
# plt.ylabel('Count')
# plt.title(r'$\mathrm{RON\ of\ Blend\ Fuels}$') 
# plt.axis([85, 110, 0, 25]) # (x origin, x endpoint, y origin, y endpoint)
# plt.grid(True)

# plt.show()


"""

This section is for Blend MON

"""

# import numpy as np
# import matplotlib.mlab as mlab
# import matplotlib.pyplot as plt

# x = [-97,-99.6,-87,-84.7,-85.5,-85.7,-86.3,-86.5,-88.2,-89.5,-86.1,-85,-85.4,-85.3,-86.5,-88.2,-85.2,-85.4,-85.7,-88.8,-89.5,-90.1,-86,-87,-88.3,-87.3,-89.8,-92,-86.6,-88.9,-91.1,-86.2,-87.5,-88.1,-87.6,-89.4,-90.9,-87.6,-89.7,-92.6,-88.1,-90,-91.5,-88.5,-89.5,-90.4,-87.1,-89,-91.3,-87,-87.9,-88.3,-86.2,-87.3,-86.6,-86.6,-87.2,-88.3,-89.4,-88.5,-88.7,-88.9,-83.5,-83.5,-82.9,-84.5,-84.2,-85.2,-85.3,-84.1,-83.7,-83.4,-83.3,-86.4,-85.8,-85.7,-84.7,-87.9,-88.1,-88.5,-85.7,-93.2,-90.1,-91.9,-86.6,-88.7,-90.7,-85.5,-84.9,-84,-83.3,-84.9,-87.5,-82.3,-84.5,-84.8,-82.2,-83.3,-84.6,-82.8,-84,-84.8,-82.8,-83.8,-84.8,-84,-85,-85.1,-83.8,-84.6,-84.9,-82.9,-83.1,-85.1,-89.4,-89.6,-89.4,-89.5,-89.1,-89,-91.4,-92.4,-89.7,-89.7,-89.2,-88.8,-88.8,-85.8,-87.1,-87.9,-87.2,-89.2,-90.9,-86.1,-88.2,-89.4,-88.1,-87.4,-90.5,-88.4,-88.2,-91.4,-90.4,-89.8,-90.9,-90.8,-92.6,-87.3,-89.9,-93.2,-87.5,-86.7,-88.1,-88.9,-83.5,-86.2,-87.3,-83,-83.1,-85.4,-87.8]

# # the histogram of the data
# n, bins, patches = plt.hist(x, 20, facecolor='green', alpha=0.5)

# plt.xlabel('Observed MON')
# plt.ylabel('Count')
# plt.title(r'$\mathrm{MON\ of\ Blend\ Fuels}$') 
# plt.axis([-105, -80, 0, 20]) # (x origin, x endpoint, y origin, y endpoint)
# plt.grid(True)

# plt.show()


"""

This section is for Blend Sensitivity

"""

# import numpy as np
# import matplotlib.mlab as mlab
# import matplotlib.pyplot as plt

# x = [11,-0.2,15,5.6,6.1,7.5,8.5,6.6,7.9,8.7,5,7.8,8.5,4.2,5,5.1,5.5,6.5,7.4,9.3,11.3,11.5,5.1,5.5,5.1,5.6,5.7,5.2,5.5,6.4,7.4,5.7,9.3,11.1,6.5,8.2,9.4,4.9,5.7,5.9,8.1,10.4,10.5,7.9,11.4,12.2,5.5,6.7,7.1,7.1,10,11.8,10.7,12.5,19.4,10.8,6.5,9,11.1,9.6,12.7,13.1,9.2,6.2,6.6,8.8,8.3,11,9.8,8.1,6.9,5.6,6.9,10.6,7.9,6.9,9.1,12,9.6,7.5,11.6,6.8,8.2,9.1,6.1,6.3,6.8,8.5,11.8,13.4,7.3,9.3,10.1,8.6,9.9,11.8,7.8,9.3,10.7,7.6,9.7,11.8,7.3,9.2,11.2,9.4,11.8,13.3,8.7,12.3,13.8,6,6.5,10.9,11,11.5,11.2,11.5,11.4,12.1,9.7,8.9,11.3,11.4,12,12.3,7.6,6.2,6,6.5,5.3,5.8,7.4,4.6,3.5,3.5,8.3,9.5,7.3,9.6,8.4,8.2,7.4,6.6,5.9,6.6,5.9,5.3,5.9,5.1,6.6,7.8,9.9,11.6,9.2,10.7,12.5,5.5,5.7,6.4,8.7] 

# # the histogram of the data
# n, bins, patches = plt.hist(x, 20, facecolor='green', alpha=0.5)

# plt.xlabel('Observed Sensitivity')
# plt.ylabel('Count')
# plt.title(r'$\mathrm{Sensitivity\ of\ Blend\ Fuels}$') 
# plt.axis([-5, 25, 0, 30]) # (x origin, x endpoint, y origin, y endpoint)
# plt.grid(True)

# plt.show()
