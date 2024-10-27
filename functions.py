#functions

#syntax -> def functionname(arguments):

'''def add(a,b):
    print("The sum is :",a+b)
    print("The differnce is :",a-b)
    print("The product is :",a*b)
add(10,20)
add(100,200)
add(1000,2000)'''

'''def div(a,b):
    print("The intdiv is :",a//b)
    print("The floatdiv is :",a/b)
    print("The pow is :",a**b)
div(5,2)
div(8,6)
div(4,2)'''

'''def cal(a,b):
    c=a+b
    print(c)
cal(3,4)'''

'''def cal():
    a=int(input("Enter a value :"))
    b=int(input("Enter b value :"))
    print(a+b)
cal()'''

'''def name():
    a=input("enter first name :")
    b=input("enter last name :")
    print((a+" "+b).title())
name()'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(4,6)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
print(cal(6,8))'''

#example split bill for trip

'''def splitbill():
    a=int(input("Total no of people :"))
    b=int(input("Enter the total amount :"))
    c=b//a
    print("your bill is : ",c)
splitbill()'''

'''def splitbill():
    a=int(input("Total no of people :"))
    b=int(input("Enter the total amount :"))
    c=b//a
    return ("your bill is :" ,c)
print(splitbill())'''

'''while True:
    def splitbill():
        a=int(input("Total no of people :"))
        b=int(input("Enter the total amount :"))
        c=b//a
        return ("your bill is : ",c)
    print(splitbill())'''

'''def splitbill():
    a=int(input("Total no of people :"))
    b=int(input("Enter the total amount :"))
    c=b//a
    print("your bill is : ",c)
    splitbill()
splitbill()'''


'''def splitbill():
    a=int(input("Total no of people :"))
    b=int(input("Enter the total amount :"))
    c=b//a
    print("your bill is {}".format(c))
    print(f"your bill is {c}")
splitbill()'''

'''def splitbill():
    a=int(input("Total no of people :"))
    b=int(input("Enter the total amount :"))
    print("your bill is {}".format(b//a))
    print(f"your bill is {b//a}")
splitbill()'''

'''def value():
    a=int(input("Enter a value :"))
    b=int(input("Enter  b value :"))
    c=int(input("Choose options 1.add 2.sub 3.mul:"))
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a*b)
    else:
        print("exit")
value()'''

'''def add():
    s=a+b
    print(s)
def sub():
    s=a-b
    print(s)
def mul():
    s=a*b
    print(s)
while True:
    a=int(input("Enter a value :"))
    b=int(input("Enter  b value :"))
    c=int(input("Choose options 1.add 2.sub 3.mul:"))
    if c==1:
        add()
    elif c==2:
        sub()
    elif c==3:
        mul()'''

#Railway Ticket

'''ticket=1000
a=int(input("Enter your Gender (male/female ):"))
age=int(input("Enter your age :"))
if a=="male":
    if age>=60:
        discount=price*0.30
        discounted_price=ticket-discount
        print("")
        
    print("Train ticket amount")'''

'''while True:
    ticketprice=1000
    gen=input("Enter your gender :")
    age=int(input("Enter your age :"))
    if gen=="male":
        if age>60:
            print("Senior Citizen")
            ticketprice=ticketprice-30/100*ticketprice
            print(ticketprice)
        elif age<=60:
            print("Normal Citizen")
            ticketprice=ticketprice
            print(ticketprice)
    elif gen=="female":
        if age>60:
            print("Senior Citizen")
            ticketprice=ticketprice-50/100*ticketprice
            print(ticketprice)
        elif age<=60:
            print("Normal Citizen")
            ticketprice=ticketprice-30/100*ticketprice
            print(ticketprice)'''

#keyword arguments
'''def check(id,name,mailid):
    id=10
    name="Mouli"
    mailid="mouli@gmail.com"
    print(id,name,mailid)
check(id="id",name="name",mailid="mailid")'''

'''def check1(id,name,mailid):
    print(id,name,mailid)
check1(id="id",name="name",mailid="mailid")
check1(id=20,name="mouli",mailid="mouli@gmail.com")
check1(30,"komal","k@gmail.com")
check1("jessy","j@gmail.com",40)
check1(mailid="k@gmail.com",id=50,name="keerthi")'''

'''def employee(empname,salary,degnastion):
    print(empname,salary,degnastion)
employee(empname="empname",salary="salary",degnastion="degnastion")
employee(empname="suresh",salary=20000,degnastion="felid officer")
employee(salary=30000,degnastion="electrical officer",empname="ramesh")
employee("kumar","mechincal officer",40000)
employee("teja",60000,"head department")'''



#default arguments

'''def Grocery(item,price):
    print("item is %s"%item)
    print("price is %.2f"%price)
Grocery("bread",60)'''


'''def Grocery(item="dhal",price=200):
    print("item is %s"%item)
    print("price is %d"%price)
Grocery()'''

'''def Grocery(item,price=500):
    print("item is %s"%item)
    print("price is %d"%price)
Grocery("ghee")'''

'''def Grocery(item="sugar",price):#non default arguments follows default arguments
    print("item is %s"%item)
    print("price is %d"%price)
Grocery(100)'''


'''def cake(cakename,quantity,price):
    print("cakename is %s"%cakename)
    print("quantity is %d"%quantity)
    print("price is %d"%price)
cake("redvelevt",1,1000)'''

'''def cake(cakename="buttersotch",quantity=2,price=1200):
    print("cakename is %s"%cakename)
    print("quantity is %d"%quantity)
    print("price is %d"%price)
cake()'''

'''def cake(cakename,quantity,price=800):
    print("cakename is %s"%cakename)
    print("quantity is %d"%quantity)
    print("price is %d"%price)
cake("vanila",1)'''

'''def cake(cakename="chocalate",quantity,price):
    print("cakename is %s"%cakename)
    print("quantity is %d"%quantity)
    print("price is %d"%price)
cake(1,1000)'''


#*arguments-> * is used to unpack
'''a=[1,2,3,4,5]
print(a)
print(*a)'''

'''b=(5,6,7,8)
print(b)
print(*b)'''

'''c={3,4,5,6,7}
print(c)
print(*c)'''

'''d={"name":"mouli","year":2024}
print(d)
print(*d)'''

'''a,b,c=5,6,7
print(a)
print(b)
print(c)'''

'''a,b,c=2,3,4,5,6,7,89,10
print(a)
print(b)
print(c)'''

'''*a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c="pythoncourse"
print(a)
print(b)
print(c)'''

'''a,b,c="pyt"
print(a)
print(b)
print(c)'''

'''a,b,c="python","course","code"
print(a)
print(b)
print(c)'''

'''a,b,*c="codegnan"
print(a)
print(b)
print(*c)'''


#variable length arguments

'''def check(*a):
    print(a)
    print(type(a))
check()
b=[1,2,3,4,5,6]
check(*b)
c=(4,5,6)
check(*c)
d={4,5,6,7,8}
check(*d)
e={"name":"mouli","year":2024}
check(*e)'''

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):  #membership operator
                d=d+i
                print(d)    
check1()
check1(2,3,4,5,6)
check1(1,2,3.2,4.5)
check1(3,4,2.1,4.2,"mouli",6+9j,True,False)'''

#kwargs(**)

def check(**a):
    print(a)
    print(type(a))
check()
d={"names":["mouli","sai","bhaskar"],"status":["P","A","P"]}
check(**d)

'''def check1(**a):
    print(a)
    print(type(a))
    for i in a.keys():
    #for i in a:
        print(i)#only keys will return
check1()
e={"idnos":[10,20,30],"names":["amrutha","sathwika","mariyam"]}
check1(**e)'''


'''def check1(**a):
    print(a)
    print(type(a))
    for i in a.keys():
    #for i in a:
        print(i)#only keys will return
    for i in a.values():
        print(i)
    for i in a:
        print(a[i])#only values will return
    for i in a.items():
        print(i)
    for i in a:#both keys and values will return
        print(i,a[i])
check1()
e={"idnos":[10,20,30],"names":["amrutha","sathwika","mariyam"]}
check1(**e)'''


#both * and ** usage

'''def final(*a,**b):
    d=2#creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,6.5,7.8,6+9j,"mouli",True,False)
final(*data)
details={"idnos":[2,3,4],"names":["mounika","deepika","venu"]}
final(**details)
final(*data,**details)'''











   
    
        
    


    

        
 
    





