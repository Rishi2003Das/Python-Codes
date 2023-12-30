import numpy as np
import matplotlib.pyplot as pt

size=[45,25,10,15,5]
color=['red','orange','yellow','green','blue']
labels=["Below 10","20-40","40-60","60-80","Above 80"]

pt.pie(size,colors=color,labels=labels,startangle=90)
pt.axis('equal')

pt.title('Chart of Indian Population',color='blue')

pt.legend(title='Age group',loc='lower left')

pt.show()