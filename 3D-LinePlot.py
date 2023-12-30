from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pt
import numpy as np
fig=pt.figure()
chart=fig.add_subplot(1,1,1,projection='3d')
x,y,z=np.array([1,5,3]),np.array([6,14,9]),np.array([10,4,11])
x=np.reshape(x, (1, 3))
y=np.reshape(y, (1, 3))
z=np.reshape(z, (1, 3))
chart.plot_wireframe(x,y,z)
pt.show()