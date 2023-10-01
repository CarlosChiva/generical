import matplotlib.pyplot as plt
x= [1,2,3,4]
y =[10,20,25,30]
# plt.figure = window
fig = plt.figure()
# subplot idunno if (ad_subplot(*) parametrer to size left right bottom of graphics)
ax =fig.add_subplot(111)
#plot (axis x  , axis y,  color of line, )
ax.plot(x,y,color ="lightblue",linewidth= 3)
#scatter ([x values on axis x][y values on axis y], color of points, mark instead of circular point) 
ax.scatter([2,4,6],[5,15,25],color ='darkgreen',marker='^')
# set_xlim = x value max and minim
ax.set_xlim(1,6.5)
#plt show = show window
plt.savefig('eeee.png')
plt.show()