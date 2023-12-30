from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pt
import numpy as np
fig=pt.figure()
chart=fig.add_subplot(1,1,1,projection='3d')
x,y,z=np.array([1,5,2,25]),np.array([6,10,13,3]),np.array([10,12,11,5])
x=np.reshape(x, (1, 4))
y=np.reshape(y, (1, 4))
z=np.reshape(z, (1, 4))
chart.scatter(x,y,z,color='red',marker='o')
pt.show()