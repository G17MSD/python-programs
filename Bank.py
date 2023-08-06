print('Hello! What would you like to do?','1: check deposit','2: check withdrawal','3:check balance')
class Bank:
    def __init__(self,name,balance,number):
        self.name=name
        self.balance=balance
        self.number=number
    def display_details(self):
        print(self.name,self.balance,self.number)
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdrawal(self,amount1):
        self.balance=self.balance-amount1
    def checkbalance(self):
        print(self.balance)
gurman=Bank('Gurman',230,17080)
'''piyush=Bank('Piyush',16000,37824)
andrei=Bank('Andrei',20,69035)
rio=Bank('Rio',0,00000)
bob=Bank('Bob',378000,29075)
objects=[gurman,piyush,andrei,rio,bob]'''
while(True):
    a=int(input('Enter a choice between 1-3 here: '))
    if (a==1):
        c=float(input('Enter a deposit here: '))
        gurman.deposit(c)
    elif (a==2):
        b=float(input('Enter a withdrawal here: '))
        gurman.withdrawal(b)
    elif (a==3):
        gurman.checkbalance()
    else:
        print('Invalid input' )