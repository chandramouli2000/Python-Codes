#fromkeys()

'''a="codegnan"
print(a)

print(list(a))

print(tuple(a))

print(set(a))

#print(dict(a))

b=dict.fromkeys(a)
print(b)



b=dict.fromkeys(a,"mouli")
print(b)


b['c']="codegnan"
print(b)'''


#eval()

'''while True:
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)'''

'''while True:
    a=float(input("a value:"))
    b=float(input("b value:"))
    print(a+b)'''

'''while True:
    a=input("Data1:")
    b=input("Data2:")
    print(a+b)'''

'''while True:
    a=complex(input("a value:"))
    b=complex(input("b value:"))
    print(a+b)'''

'''while True:
    a=bool(input("a value:"))
    b=bool(input("b value:"))
    print(a+b)'''

'''while True:
    a=eval(input("a value:"))
    b=eval(input("b value:"))
    print(a+b)'''

#[],(),{}

'''a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))'''


#zip()->we can combine multiple collections into one collection

'''a=[10,20,30,40,50]
names=["jyothi","susmitha","swathika","haritha","lasaya"]
print(a+names)

b=zip(a,names)
print(b)

c=dict(zip(a,names))
print(c)

d=list(zip(a,names))
print(d)

e=tuple(zip(a,names))
print(e)

f=set(zip(a,names))
print(f)'''


#enumerate()-> we can give counter to the collections

'''names=["prem","durgarao","naveed","vijay","bhargava"]
for i in range(len(names)):
               #print(i)
            print(i,names[i])

b=dict(enumerate(names))
print(b)

c=dict(enumerate(names,100))
print(c)'''


#annnonymous functions->(nameless functions)
#write a function to calculate 2*x+5 where x=5
'''def cal():
    x=5
    y=2*x+5
    print(y)
cal()

def f(x):
    print(2*x+5)
f(5)

def f(x):
    return 2*x+5
print(f(5))

def f():
    x=int(input("x value"))
    print(2*x+5)
f()'''


#syntax -> a=lambda arg:expr

'''a=lambda x:2*x+5
print(a(5))

a=int(input("a value :"))
b=lambda x:2*x+5
print(b(a))'''


'''a=10
b=20
c=lambda a,b:a+b
print(c(a,b))

a=lambda a,b:a+b
print(a(6,7))

a=int(input("a value :"))
b=int(input("b value :"))
c=lambda a,b:a+b
print(c(a,b))'''

#codegnan
#CODEGNAN 
'''a=lambda x:"CODEGNAN"
print(a("CODEGNAN"))

a="codegnan"
b=lambda a:a.upper()
print(b(a))

a=lambda a:a.upper()
print(a("codegnan"))


a=input("Data1 :")
b=lambda a:a.upper()
print(b(a))'''

#python course
#Python Course

'''a=lambda a:a.title()
print(a("python course"))'''


#firstname & lastname
'''a=input("first name:")
b=input("last name :")
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

'''a,b=(x for x in input("enter the name :").split(','))
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

'''a,b=input("enter the name :").split(',')
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''


#filter()

'''a=[10,25,20,45,30,40,55,60,75]
if a%2==0:
    print(a)'''


'''a=[10,25,20,45,30,40,55,60,75]
for i in a:
    if i%2==0:
        print(i)'''

'''a=[10,25,20,45,30,40,55,60,75]
b=list(filter(lambda a:a%2==0,a))
print(b)'''

'''a=[10,25,20,45,30,40,55,60,75]
b=list(filter(lambda a:a%2!=0,a))
print(b)'''


'''a=[(),[],set(),None,{}," ",5,7.8,"python",3+8j,True,False]
b=list(filter(None,a))
print(b)'''

#map()-> each object from a collection and forms a new collection

'''a=[2,5,9,12,15,30,80]
b=[1,3,20,5,7,50,4]

c=list(map(max,a,b))
print(c)

d=list(map(min,a,b))
print(d)'''


'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=[x for x in input("enter the data").split(',')]
print(a+b)'''

'''a,b=input("enter the names").split(',')
print(a+b)'''

'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''a,b=int(input("enter the values")).split(',')#error code
print(a+b)'''

'''a,b=map(int,input("enter the values :").split(','))
print(a+b)'''

'''a=[1,2,3,4,5,6,7,8,9]
b=list(map(lambda x:x**2,a))
print(b)'''

a=[11,22,33,44,55,66,77]
b=list(map(lambda x:x%2,a))
print(b)












