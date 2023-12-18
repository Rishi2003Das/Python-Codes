import matplotlib
import matplotlib.pyplot as pt
fig=pt.figure()
pt.title("Rainfall measurement")
pt.xlabel("Last 10 Days in November")
pt.ylabel("Rainfall in cm")
rec=fig.patch.set_facecolor('green')
x=[1,3,5,7,10]
y=[7,10,20,25,50]
graph1=fig.add_subplot(1,1,1,facecolor='black')
graph1.plot(x,y,'red',linewidth=2.0)
pt.show()