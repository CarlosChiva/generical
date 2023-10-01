#1.- Prepare data
import numpy as np
x=np.linspace(0,10,100)
y= np.cos(x)
z = np.sin(x)
#from matplotlib.cbook import get_sample_data
#img= np.load(get_sample_data('axes_grid/bivariate_normal.npy'))
#2.- create plot
import matplotlib.pyplot as plt
fig=plt.figure()
fig2= plt.figure(figsize=plt.figaspect(2.0))
# axes
fig.add_axes([1,2, 3,4])
ax1= fig.add_subplot(221)
ax3= fig.add_subplot(212)
# another way to make graphics nrows n graphics in row and ncol n graphics in column n
fig3, axes= plt.subplots(nrows=2,ncols=2)
#fig4, axes2= plt.subplots(ncols=3)
#3.- plotting Routenes
lines1=ax1.plot(x,y)
ax1.scatter(x,y)
axes[0,0].bar([1,2,3],[3,4,5])
axes[1,0].barh([0.5,1,2.5],[0,1,2])
axes[1,1].axhline(0.45)
axes[0,1].axvline(0.65)
ax1.fill(x,y,color='blue')
ax1.fill_between(x,y,color='yellow') 
lines3=ax3.plot(x,y)
ax3.scatter(x+1,y+1)
plt.show()