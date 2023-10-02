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
#fig2= plt.figure(figsize=plt.figaspect(2.0))
# axes
fig.add_axes([1,2, 3,4])
ax1= fig.add_subplot(221) # elemento donde se fija 
ax3= fig.add_subplot(212)
# another way to make graphics nrows n graphics in row and ncol n graphics in column n
fig3, axes= plt.subplots(nrows=2,ncols=2)
#fig4, axes2= plt.subplots(ncols=3)
#3.- plotting Routenes
lines1=ax1.plot(x,y)
 #ax1.scatter(x,y)
axes[0,0].bar([1,2,3],[3,4,5]) #Plot vertical rectangles (constant width)
axes[1,0].barh([0.5,1,2.5],[0,1,2]) # Plot horiontal rectangles (constant height)
axes[1,1].axhline(0.45)  #Draw a horizontal line across axes
axes[0,1].axvline(0.65)  # Draw a vertical line across axes
 #ax1.fill(x,y,color='blue') # Draw filled polygons
 #ax1.fill_between(x,y,color='yellow') # Fill between y-values and 0
#lines3=ax3.plot(x,y)
ax3.scatter(x+1,y+1)

# 4.- Customize plot

plt.plot(x,x,x,x**2,x,x**3)
#ax1.plot(x,y,alpha=0.4) #  line light-gray in graphic
#ax1.plot(x,y,c='k')# line 'k' black color in graphic
#--- Image----
#fig.colorbar(im,orientation='horizontal')
#im = ax1.imshow(img,cmap='seismic')

#markers no because imagen

# linestyles

#plt.plot(x,y,linewidth=4.0) # red in line
#plt.plot(x,y,ls='solid')
#plt.plot(x,y,ls='--') # line interlined '--'
plt.plot(x,y,'--',x**2,y**2,'-.') # formater first dates with -- an other dates with -.
plt.setp(lines1,color='r',linewidth=4.0) # add style of 'lines1' color red and width of 4
ax1.text(1,-2.1,'Example Graph',style='italic') # doesnt work
ax1.annotate("Sine",xy=(8, 0),xycoords='data',xytext=(10.5, 0),textcoords='data',arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),) #text of anotation, point in graphic
plt.show()