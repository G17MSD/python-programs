'''names=['Andrei','Alvin','Alex','Gurman','Piyush']
count=0
a=input('Enter a letter here: ')
for i in range(len(names)):
    if (names[i][0]==a):
        count=count+1
print(count)'''
a=input('Enter a sentence here: ')
new_input=a.split(' ')
new_input.reverse()
print(new_input)
new_names=' '.join(new_input)
print(new_names)