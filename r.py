import math
import matplotlib.pyplot as p
from prettytable import PrettyTable
x=[]
y=[]
n=int(input("Enter the size of the dataset : "))
x1=0
y1=0
for i in range(0,n):
    print("Enter the value of X",(i+1)," :")
    x1=int(input())
    print("Enter the value  of Y",(i+1)," :")
    y1=int(input())
    x.append(x1)    
    y.append(y1)
sx2=0
sy2=0
x_n=0
y_n=0
xy=0
x_y=0
for i in range(0,n):
    sx2=sx2+x[i]**2
    sy2=sy2+y[i]**2
    x_n=x_n+x[i]
    y_n=y_n+y[i]
    xy=xy+(x[i]*y[i])
x_y=(x_n*y_n)/n
ssx=sx2-((x_n**2)/n)
ssy=sy2-((y_n**2)/n)
sp=xy-x_y
r=(sp)/(math.sqrt(ssx*ssy))
b=r*(math.sqrt((ssy/ssx)))
a=(y_n/n)-(b*(x_n/n))
#predictingequ
Y_1=[]
y_1=0
for i in range(0,n):
    y_1=int(b*x[i]+a)
    Y_1.append(y_1)
if(r>0):
    print("The DATASET is positively related and the r value is : ",r)
elif(r<0):
    print("The DATASET is negatively related and the r value is : ",r) 
else:
    print("The DATASET has no relationship ")
myt = PrettyTable(["X","ORIGINAL Y VALUE","PREDICTED Y VALUE "])
for i in range(0,n):
    myt.add_row([x[i],y[i],Y_1[i]])
print(myt)
p.plot(x,y)
p.plot(x,Y_1)
p.legend(["ORIGINAL","PREDICTED"],loc="lower right")
p.show()  
    
