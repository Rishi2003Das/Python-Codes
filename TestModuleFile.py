#Test File
import time
import random
import turtle
import sys
names=["Rishi","Priyam","Sushrut","Agnish","Surit","Agnik"]#list
print(random.randint(100,200))
print(random.choice(names))
print(random.shuffle(names))
line= sys.stdin.readline()
print(line)
print(sys.stdout.write("I am very good boy with black hair!!!"))
print(time.asctime())
t=turtle.Pen()
for i in range(0,8):
    t.left(45)
    t.forward(10)
