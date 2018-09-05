"""
We need to make graphs for RON and the other fuel properties
(see the graph on page 3/9 of the BioCompoundML paper for
reference). We will be using matplotlib to create bar graphs. 

"""

"TEST: "
# import matplotlib.pylot as plt; plt.rcdefaults()
# import numpy as np
# import matplotlib.pyplot as plt 
# import plotly.plotly as py # tools to communicate with Plotly's server (may need api key)

# pure_surface_tension = plt.figure()
# plt.hist([2,3,4], bins=[5,6,7,8]) 
# plot_url = py.plot_mpl(pure_surface_tension, filename='pure-surface-tension') 

"This is another test: UPDATE: WORDS PERFECTLY :D"
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()
