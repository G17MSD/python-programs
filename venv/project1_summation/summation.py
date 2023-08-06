f=open('data.txt','r+')
a=f.readlines()
list=[]
for i in range(len(a)):
    b=int(a[i][2])+int(a[i][0])
    list.append(b)
print(list)
f=open('output.txt','w+')
for i in range(len(list)):
    list[i]=str(list[i])+'\n'
f.writelines(list)

