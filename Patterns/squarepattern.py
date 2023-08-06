'''for i in range(5):
    print('# '*5)

for i in range(5):
    for j in range(5):
        print('#', end=' ')
    print()

for i in range(5):
    for j in range(5):
        print(j, end=' ')
    print()
    0 1 2 3 4
    0 1 2 3 4
    0 1 2 3 4
    0 1 2 3 4
    0 1 2 3 4
i=0
j=0 : 0
j=1 : 1
j=2 : 2
j=3 : 3
j=4 : 4
i=1
j=0 : 0
j=1 : 1
j=2 : 2
j=3 : 3
j=4 : 4
i=2
j=0 : 0
j=1 : 1
j=2 : 2
j=3 : 3
j=4 : 4
i=3
j=0 : 0
j=1 : 1
j=2 : 2
j=3 : 3
j=4 : 4
i=4
j=0 : 0
j=1 : 1
j=2 : 2
j=3 : 3
j=4 : 4


for i in range(5):
    for j in range(5):
        print(i, end=' ')
    print()
for j in range(5):
    for i in range(j+1):
        print('*',end='')
    print()

j=0
i=0 : * 
j=1
i=0 : *
i=1 : *
j=2
i=0 : *
i=1 : *
i=2 : *
j=3
i=0 : *
i=1 : *
i=2 : *
i=3 : *
j=4
i=0 : *
i=1 : *
i=2 : *
i=3 : *
i=4 : *

for j in range(1,6):
    for i in range(j):
        print(j,end='')
    print()
j=1
i=1 : 1
j=2
i=2 : 2
i=2 : 2
j=3
i=3 : 3
i=3 : 3
i=3 : 3
j=4
i=4 : 4
i=4 : 4
i=4 : 4
i=4 : 4
j=5
i=5 : 5
i=5 : 5
i=5 : 5
i=5 : 5
i=5 : 5
for j in range(8):
    for i in range(j+1):
        print(i,end='')
    print(i)

for i in range(1, 13):
    print(f"Multiplication table for {i}:")
    for j in range(1, 13):
        product = i * j
        print(f"{i} x {j} = {product}")
    print()

I=1 
Print("Multiplication table for 1: ") 
J=1 
Product= 1*1 =1 
Print("1 x 1 = 1") 

I=1 
J=2 
Product= 1*2=2 
Print("1 x 2 = 2") 

I=1 
J=3 
Product=1*3=3 
Print("1 x 3 = 3") 

I=1 
J=4 
Product=1*4=4 
Print("1 x 4 = 4") 

I=1 
J=5 
Product=1*5=5 
Print("1 x 5= 5") 

I=1 
J=6 
Product=1*6=6 
Print("1 x 6= 6") 

I=1 
J=7 
Product=1*7=7 
Print("1 x 7 =7") 

I=1 
J=8 
Product=1*8=8 
Print("1 x 8 =8") 

I=1 
J=9 
Product=1*9=9 
Print("1 x 9 =9") 

I=1 
J=10 
Product=1*10=10 
Print("1 x 10=10") 

I=2
print("Multiplication table for 2:") 
J=1 
Product=2*1=2 
Print("2 x 1=2") 

I=2 
J=2 
Product=2*2=4 
Print("2 x 2=4") 

I=2 
J=3 
Product=2*3=6 
Print("2 x 3=6") 

I=2 
J=4 
Product=2*4=8 
Print("2 x 4=8") 

I=2 
J=5 
Product=2*5=10 
Print("2 x 5=10") 

I=2 
J=6 
Product=2*6=12 
Print("2 x 6=12") 

I=2 
J=7 
Product=2*7=14 
Print("2 x 7=14") 

I=2 
J=8 
Product=2*8=16 
Print("2 x 8=16") 

I=2 
J=9 
Product=2*9=18 
Print("2 x 9=18") 

I=2 
J=10 
Product=2*10=20 
Print("2 x 10=20")

list=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j],end=' ')
    print()'''

'''#Write a program that generates a sequence of random numbers using nested loops.
#The user should be able to specify the length of the sequence and the range of possible values as input
import random
for i in range(1,15):
    number='''