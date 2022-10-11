import math
from prettytable import PrettyTable
data =[]
n=int(input("Enter the No of data  : "))
a=0
for i in range(0,n):
    print("Enter the data ",(i+1)," :")
    a=int(input())
    data.append(a)
data.sort()
#mean
mean=sum(data)/n
c=0
ct=[]
du=0
#mode
for i in range(0,n):
    if(du==data[i]):
        c=0
        ct.append(c)
        continue
    for j in range(0,n):
        if(data[i]==data[j]):
            c+=1
    if(c==1):
        c=0
        du=0
    elif(c>1):
        du=data[i]
    else:
        pass
    ct.append(c)
    c=0

m1=max(ct)
no_mx=ct.count(m1)
uni_mo=0
if(no_mx==1):
    for i in range(0,n):
        if(m1==ct[i]):
            uni_mo=data[i]
mu_mo=[]
if(no_mx>=2):
    for i in range(0,n):
        if(m1==ct[i]):
            mu_mo.append(data[i])
mu_mo1=set(mu_mo)
mu_mo2=list(mu_mo)    
#median
median=0
if((len(data)%2)==0):
    median=float((data[(int(len(data)/2))-1]+data[((int(len(data)/2)))])/2)
elif(len(data)%2==1):
    median=data[(int(len(data)/2))]
else:
    pass
#range
min_val=data[0]
max_val=data[n-1]
rang_val=int((max_val))-int((min_val))  
#variance
s=0
for i in range(0,n):
    s=s+((data[i]-mean)**2)
variance=float(s/n)
#STANDARDDEVIATION
SD =math.sqrt((s/(n-1)))
myt=PrettyTable(["MEAN","MEDIAN","VARIANCE","RANGE","STANDARD DEVIANTION"])
myt.add_row([mean,median,variance,rang_val,SD])
print(myt)
if(no_mx==1):
    print("THE MODE VALUE IS: ",uni_mo)
elif((no_mx>1)and(len(mu_mo2)!=n)):
    for i in range(0,len(mu_mo2)):
        print("MODE ",(i+1),":",mu_mo2[i])
else:
    print("No Mode")

