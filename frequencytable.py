import matplotlib.pyplot as plt
from prettytable import PrettyTable
data =[]
n=int(input("Enter the no  of data: "))
for i in range(0,n):
    print("Enter a data of ",(i+1))
    k=int(input())
    data.append(k)
#sort the data
data.sort()
min_val=data[0]
max_val=data[n-1]
rang_val=int((max_val))-int((min_val))
ci=int((rang_val)/10)
c_i1=ci
if(ci<=5):
    ci=5
else:
    ci=10
r=[]
d=data[0]
c=0
min_rem=0
l_c_mi_r=0
if(data[0]==0):
    min_rem=0
else:
    min_rem=(d%10)
if(min_rem<=ci):
    l_c_mi_r=data[0]-min_rem
elif(min_rem>ci):
    min_rem=min_rem-ci
    l_c_mi_r=data[0]-min_rem
else:
    pass
mx_rem=0
if(data[n-1]==0):
    mx_rem=0
else:
    mx_rem=(d%10)
if(mx_rem<=ci):
    max_val_low=data[n-1]-mx_rem
elif(mx_rem>ci):
    mx_rem=mx_rem-ci
    max_val_low=data[n-1]-mx_rem
else:
    pass
low_range=[]
high_range=[]
l_c_mx_r=l_c_mi_r+(ci-1)
max_val_high=max_val_low+ci
last_rng_setv=max_val_high+ci
b=l_c_mx_r+ci
for i in range((l_c_mx_r),last_rng_setv,ci):
    k=0
    low_range.append(k)
    high_range.append(k)
low_range[0]=l_c_mi_r
high_range[0]=l_c_mx_r
g=1
for i in range((l_c_mx_r+ci),last_rng_setv,ci):
    low_range[g]=low_range[g-1]+ci
    high_range[g]=high_range[g-1]+ci
    g+=1
i=0
f=[]
k=0
for i in range((l_c_mx_r),last_rng_setv,ci):
    k=0
    f.append(k)
count=0
for i in range(0,len(low_range)):
    for j in range(0,len(data)):
        if(data[j])>=low_range[i]:
            if(data[j]<=high_range[i]):
                count=count+1
    if(count==0):
        f[i]=0
    else:
        f[i]=count
    count=0
#relativefrequency
rf=[]
tot_f=sum(f)
for i in range(0,len(low_range)):
    o=round((f[i])/(tot_f),2)
    rf.append(o)
#cumulativefrequency
cf=[]
cf.append(f[0])
for i in range(1,len(low_range)):
    o=f[i]+cf[i-1]
    cf.append(o)
#commulativepercentile
cf_p=[]
for i in range(0,len(low_range)):
    o=round(((cf[i]*100)/sum(f)))
    cf_p.append(o)
#reallimits
real_mi=[]
real_mx=[]
for i in range((l_c_mx_r),last_rng_setv,ci):
    k=0
    real_mi.append(k)
    real_mx.append(k)
l=0
h=0
i=0
for j in range((l_c_mx_r),last_rng_setv,ci):
    real_mi[h]=low_range[h]-0.5
    real_mx[h]=high_range[h]-0.5
    h+=1
myt=PrettyTable(["DataRange","Frequency Value","Reall Limits","RelativeFrequency","CummulativeFrqeuncy","CummulativePercetinle "])
for t in range(0,len(low_range)):
    myt.add_row([(str(low_range[t])+"-"+str(high_range[t])),f[t],(str(real_mi[t])+"-"+str(real_mx[t])),rf[t],cf[t],cf_p[t]])

print(myt)
x=[]
for i in range(0,len(f)):
    x.append((str(low_range[i])+"-"+str(high_range[i])))
print("")
print("THE RANGE VALUE IS :",rang_val)
print("THE CLASS INTERVAL IS: ",int(ci))

print("The Relative Frequency is :  ",round(sum(rf),1))
plt.bar(x,f)
plt.show()
