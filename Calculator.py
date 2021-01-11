def perform(a):
    print("\nWhat to do (+, -, *, /)")
    y=input()
    if(y=="+"):
        b=int(input("\nEnter number 2 : \n"))
        res=add(a,b)
        print("Your Result is :",res)
    elif(y=="-"):
        b=int(input("\nEnter number 2 : \n"))
        res=sub(a,b)
        print("Your Result is :",res)
    elif(y=="*"):
        b=int(input("\nEnter number 2 : \n"))
        res=mul(a,b)
        print("Your Result is :",res)
    elif(y=="/"):
        b=int(input("\nEnter number 2 : \n"))
        res=div(a,b)
        print("Your Result is :",res)
    perform(res)

def input1():
    a=int(input("Enter number 1 : "))
    perform(a)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

while(1):
    x=int(input("\nPress 1 to start\nPress 2 to Stop\n"))
    if(x==1):
        input1()
    elif(x==2):
        exit()
        
    
