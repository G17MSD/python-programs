'''class Student:
    def __init__(self,name,ID,marks):
        self.name=name
        self.ID=ID
        self.marks=marks
    def display(self):
        print('Name: ',self.name)
        print('ID: ',self.ID)
        print('Marks: ',self.marks)
object=Student('Thomas',398,[34,23,56,78,49])
object1=Student('Bob',492,[87,98,67,99,89])
object2=Student('Piyush',280,[78,86,74,45,32])
object3=Student('Andrei',389,[0,13,56,43,22])
object4=Student('Gurman',999,[99,89,78,67,59])
print(object.name,object.ID,object.marks)
print(object1.name,object1.ID,object1.marks)
print(object2.name,object2.ID,object2.marks)
print(object3.name,object3.ID,object3.marks)
print(object4.name,object3.ID,object3.marks)

#Write a program to design a class named Human. human class will have 2 attributes name
# #and age create 3 objects of human class to pass the name and ages also create a method to join
# #the first letter of each name to create a new string and add the ages to create a new number.
# #Join this string and the number with add the rate kbc
class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
object=Human('Piyush',26)
object1=Human('Gurman',14)
object2=Human('Rio',60)
names=object.name[0]+object1.name[0]+object2.name[0]
ages=object.age+object1.age+object2.age
print(str(ages)+names,'@gmail.com')

class Car:
    def __init__(self,company,car,maxspeed):
        self.company=company
        self.car=car
        self.maxspeed=maxspeed
        def display(self):
            print('Company: ',self.company)
            print('Car: ',self.car)
            print('Maxspeed: ',self.maxspeed)
object=Car('Lamborghini',140,150)

class Human:                    #the class is which category it is
    def __init__(self,name,age,city):        #init is the name of the function
        self.name=name
        self.age=age
        self.city=city
    def display(self):
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('City: ',self.city)
gurman=Human('Gurman',14,'Bradford')
piyush=Human('Piyush',26,'Dehradun')
andrei=Human('Andrei',13,'Manchester')
gurman.display()
piyush.display()
andrei.display()
#How to call a method?
#object.method()
#1.Line 48
#2.Line 49
#3.Line 53
#4.Line 54
#5.Line 55
#6.Line 50
#7.Line 51
#8.Line 52
#LIST OF ATTRIBUTES:
#-Name
#-age
#-City
#METHODS:
#-display()
#Write a Python program to read a file line by line and display each line.
f=open('file.txt','r+')
a=f.readlines()
for i in range(len(a)):
    print(a[i])
#Write a Python program to count the number of lines in a text file.
f=open('file.txt','r+')
a=f.readlines()
print(len(a))
#Write a Python program to append text to an existing file and display the contents of the file.
destination='Text_file.txt'
f=open('Text_file.txt','w+')
f.writelines(['andrei puss in boots'])
#Write a Python program to read a file and convert all the text to uppercase.
f=open('file.txt','r+')
a=f.readlines()
print(a.upper())
#Write a Python program to remove the newline character from a text file.
f=open('File.txt','r+')
a=f.readlines()
a.remove('\n')
print(a)
#Write a program that reads a file and prints the number of lines,characters and words.
f=open('File.txt','r+')
a=f.readlines()
count=0
countspace=0
for i in range(len(a)):
    count=count+1
print(count,'is the number of lines.')
f.seek(0)
b=f.read()
for g in range(len(b)):
    if (b[g]==' ' or b[g]=='\n'):
        countspace=countspace+1
print(countspace,'is the number of words')
print(len(b)-countspace,'is the number of characters')
num=0
alphabet=int(input('Enter a number here: '))
if (alphabet>=5 and alphabet<=30):
    print(chr(alphabet+60))
else:
    print('Invalid number')
while (True):
    a = input('Enter a word here: ')
    if (len(a)<2):
        print('Invalid input')
    else:
        print(a[0],'-',a[-1])
#Write a program that takes in a string as input and outputs the string with all of its vowels removed. If the input string contains no vowels, the program should output an error message.
#Here are some example inputs and outputs:
#Input: "hello world" Output: "hll wrld"
#Input: "computer science" Output: "cmpt scnc"
#Input: "xyz" Output: "Invalid input"
def count_vowels(count):
    a=input('Enter a word here: ')
    for i in range(len(a)):
        if (a[i]=='a' or a[i]=='e' or a[i]=='i'or a[i]=='o'or a[i]=='u'):
            count=count+1
    print(count)
count_vowels(0)
number = int(input("Enter a number: "))
sum =0
while number>0:
    digit = number%10
    sum = sum+1
    number = number//10
print("The sum of the digits of the input number is", sum)
a=input('Enter a string here: ')
count=0
sum=0
for i in range(len(a)):
    if (a[i].islower()):
        count=count+1
    elif (a[i].isupper()):
        sum=sum+1
print(count,'is the number of lowercase letters')
print(sum,'is the number of uppercase letters')
#Create a function that replaces all the vowels in a string with a specified character.
a=input('Enter a string here: ')
for i in range(len(a)):
    if (a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
        a=a.replace('a','?')
        a=a.replace('e',',')
        a=a.replace('i','!')
        a=a.replace('o','*')
        a=a.replace('u','%')
        print(a)
a=input('Enter a string here: ')
if (a==a[::-1]):
    print(a,'is the same')
else:
    print('it is not the same')
a=str(input('Enter a card number here: '))
for i in range(len(a)):
    if(len(a)==7):
        a=a.replace(a[0],'*')
        a=a.replace(a[1],'*')
        a=a.replace(a[2],'*')
print(a)
def card_hide(numbers):
    a=numbers[-4::1]
    i=len(numbers)-4
    b=i*'*'
    print(b+a)
card_hide('1234123456785678')
def replace_vowels(vowels,case):
    vowels=vowels.replace('a',case)
    vowels=vowels.replace('e',case)
    vowels=vowels.replace('i',case)
    vowels=vowels.replace('o',case)
    vowels=vowels.replace('u',case)
    print(vowels)
replace_vowels('Shakespeare','%')
def circle_or_square(radius,area):
    circumference=2*3.14*radius
    perimeter=(area**2)*4
    if(circumference>perimeter):
        print(True)
    else:
        print(False)
circle_or_square(12,340)
def damage(damage,speed,time):
    if (time=='Seconds'):
        print(damage*speed)
    elif(time=='minutes'):
        print(damage*speed*60)
    elif(time=='hours'):
        print(damage*speed*60*60)
damage(2,100,'hours')
def integer_boolean(number):
    a=[]
    for i in range(len(number)):
        if (number[i]=='1'):
            a.append(True)
        elif (number[i]=='0'):
            a.append(False)
    print(a)
integer_boolean("100101")
integer_boolean("10")
integer_boolean("001")
def step_by_step(character):
    b=''
    num=0
    for i in range(len(character)):
        if (character[i].islower()):
            b=b+character[i].upper()
            num=num+1
        elif (character[i].isupper()):
            b=b+character[i].lower()
            num=num+1
        else:
            b=b+character[i]
    print(character,'-original')
    print(b,'-changed')
    print(num,'-capitals that have been changed')
step_by_step('AAAAAAAAbbbbccccc')
def difference(numbers):
    a=1
    for i in range(len(numbers)):
        if (numbers[i]>a):
            a=a+numbers[i]
difference([2,5,4,6,7,16,14])
sites={'London Eye':[5, 27.0],'London T ran sport Museum':[2, 18.50],'Emirates Air Line Cable Car': [4, 5.0], 'Tower of London': [3, 28.90]}
for i in range(len(sites))
list_1=[1,2,2,3,6,7,9,2,0,2,5,6]
count=0
a=int(input('Enter a number here: '))
for i in range(len(list_1)):
    if (list_1[i]==a):
        count=count+1
print(count)
menu=
Options:  
1. Add an attendee  
2. Remove an attendee  
3. View the list of attendees  
4. Check if an attendee is present  
5. Exit
a=[]
while (True):
    num = int(input('Enter a number here: '))
    if (num==1):
        choice=input('Enter a name here: ')
        a.append(choice)
    elif (num==2):
        details=int(input('Enter the position you would like to remove: '))
        a.pop(details)
    elif (num==3):
        print(a)
    elif (num==4):
        choice=input('Enter a name here: ')
        if (choice==a):
            a.append(choice)
            print(a)
        elif (num==5):
            break
a=[10,56,27,89,52,79,99]
largest=a[0]
smallest=a[0]
sum=0
for i in range(len(a)):
    sum=sum+a[i]
    if (a[i]>largest):
        largest=a[i]
    elif (a[i]<smallest):
        smallest=a[i]
print(sum/len(a),'is the average grade')
print(largest,'is the highest grade')
print(smallest,'is the lowest grade')
a=[]
while (True):
    num=int(input('Enter a number here: '))
    if (num==1):
        choice=input('Enter a item here: ')
        a.append(choice)
    elif (num==2):
        details=int(input('Enter the position you would like to remove: '))
        a.pop(details)
    elif (num==3):
        print(a)
    elif (num==4):
        choice=input('Enter a item here: ')
        if (choice==a):
            a.append(choice)
            print(a)
    elif (num==5):
        break
a=[]
while (True):
    num = int(input('Enter a number here: '))
    if (num==1):
        choice=input('Enter a item here: ')
        a.append(choice)
    elif (num==2):
        remove=int(input('Enter the position you would like to remove: '))
        a.pop(remove)
    elif (num==3):
        print(a)
    elif (num==4):
        choice=input('Enter a item here: ')
        if (choice==a):
            a.append(choice)
            print(a)
    elif (num==5):
        break'''