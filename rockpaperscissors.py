f=open('File.txt','r+')
a=f.readlines()
count=0
for i in range(len(a)):
    print(a[i])