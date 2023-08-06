f=open('data.txt','r+')
a=f.readlines()
for i in range(len(a)):
    if (a[i]=='PUSS' or a[i]=='Puss'):
