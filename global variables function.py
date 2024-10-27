#global and local variables
#first case of global variable

'''a=6
def check():
    print("inside the value is",a)
check()
print("outside the value is",a)'''


#second case of global variable

'''a=10
def check1():
    a=5 #creating a variable
    a=a**2
    print("inside the value is",a)
check1()
print("outside the value is",a)'''

#third case of both global & local variables

'''a=2
#b=4 define variable outside then it print otherwise it shows error
def check2():
    a=5 #creating a variable
    print("inside value is",a)
    a=10
    print("Updated value is",a+5)
    b=13#local variable
    b=b+a
    print("value of b is",b)
check2()
print("value of a is",a)
print("value of b is",b)'''


#usage of global keyword
'''a=6
b=3
def final():
    global a
    print("inside value is",a)
    a=7
    print("updated value is",a)
    #global b
    b=12#local variable
    b=b+a
    print("value of b is",b)
final()
print("value of a is",a)
print("value of b is",b)'''


#generators

'''a=[i*3 for i in range(16)]
print(a)'''

'''a=(i*3 for i in range(16))
print(a)
print(type(a))'''

'''a=(i*3 for i in range(16))
print(*a)
print(type(a))'''

'''a=(i*3 for i in range(16))
print(list(a))

a=(i*3 for i in range(16))
print(tuple(a))

a=(i*3 for i in range(16))
print(set(a))

a=(i*3 for i in range(16))
print(dict(a))'''

#yield and return

'''a,b=[int(x) for x in input("Enter the values :").split(',')]
def gen(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*gen(a,b))'''


'''a,b=[int(x) for x in input("Enter the values :").split(',')]
def gen(a,b):
    while a<b:
        a=a+1
        yield a
print(*gen(a,b))'''


'''a,b=[int(x) for x in input("Enter the values :").split(',')]
def gen(a,b):
    while a<b:
        a=a+1
        return a
print(gen(a,b))'''

'''a,b=[int(x) for x in input("Enter the values :").split(',')]
def gen(a,b):
    while a<b:
        a=a+1
    return a
print(gen(a,b))'''


'''a,b=(int(x) for x in input("Enter the values :").split(','))
def gen(a,b):
    while a<b:
        a=a+1
        return a
print(gen(a,b))'''

#yield v/s return

'''def mygen():
    #return "python"
    #return "java"
    #return "c"
    return "python","java","c"
print(*mygen())'''


'''def mygen():
    yield "A"
    yield "B"
    yield "C"
print(*mygen())


#next()->which will gives successive iteration

d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))'''


#max(),min(),sum(),next(),print(),type(),range(),input(),len()

'''a=2,3,4,5,6,7
print(sum(a))
print(max(a))
print(min(a))
print(len(a))

b=6
print(type(b))


c=input()
print(c)'''

for i in range(16):
    print(i)
    



        



