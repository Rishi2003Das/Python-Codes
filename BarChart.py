import numpy as np
import matplotlib.pyplot as pt
pos= np.arange(7)+1
pt.barh(pos,(2,4,3,5,16,9,2),align='center',color='red')

pt.tick_params(axis='x',color='green')
pt.tick_params(axis='y',color='green')

pt.title("Height of college students in feets",color='blue')
pt.xlabel("Number of students",color='green')
pt.ylabel("Height of students",color='green')

feet= ["1feet","2feet","3feet","4feet","5feet","6feet","7feet"]# The array
pt.yticks(pos,feet)

pt.show()