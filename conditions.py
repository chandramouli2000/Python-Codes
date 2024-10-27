#conditions
#if condition by using comparision operators

'''a=10
b=12
if a<b:
    print("lower")'''

    
'''a=10
b=12
if a>b:
    print("greater")'''

    
'''a=10
b=12
if a<=b:
    print("True")'''

'''a=10
b=12
if b>=a:
    print("greater")'''

'''a=12
b=12
if a==b:
    print("equal")'''

'''a=10
b=12
if a!=b:
    print("not equal")'''

'''a=int(input("enter the a value"))
b=int(input("enter the b value"))
if a>b:
    print("greater")'''

'''a=int(input("a value"))
if a<30:
    print("lesser")'''

'''a=input("enter the name")
if a=="mouli":
    print("match")'''

#if condition by using logical operators

'''a=4
b=8
if a<b and b>a:
    print("true")'''

''''a=3
b=7
if a>=b and a<=b:
    print("false")'''

'''a=5
b=10
if a!=b and a==b:
    print("not equal")'''

'''a=6
b=6
if a!=b or a==b:
    print("equal")'''

'''a=30
b=50
if a<b or b>a:
    print("less")'''

'''a=15
b=25
if a>=b or b>=a:
    print("greater")'''

#if condition by using idetify operators

'''a=4
if type(a) is int:
    print("is int")'''

'''a=7.5
if type(a) is not float:
    print("not float")'''

'''a=5
if a is 5:
    print("True")'''

'''a=7
b=7
if a is b :
    print("true")'''

'''a=[1,2,3,4,5]
b=[1,2,3,4,5]
if a[2] is b[2]:
    print("true")'''

#if condition by using membership operators

'''a=2,3,4,5,6,7,8
if 5 in a:
    print(5)'''

'''a=7,8,9,1,2
if 10 not in a:
    print(10)'''

'''a=int(input("enter the a value"))
b=[2,3,4,5,6]
if a in b:
    print(a)'''

#if-else
'''a=4
b=6
if a<b:
    print("less")
else:
    print("greater")'''

'''a=4
b=6
if a>b:
    print("less")
else:
    print("greater")'''

'''a=4
if type(a) is int:
    print("int")
else:
    print("not int")'''

'''a="python"
if type(a) is str:
    print("string")
else:
    print("not a string")'''

#if-else using membership operator
'''a=2,3,4,5
if 2 in a:
    print("true")
else:
    print("false")'''

'''a=int(input("enter the values"))
b=2,4,6,8
if a in b:
    print(a)
else:
    print(b)'''

'''a=int(input("enter a vlues"))
b=int(input())
if a<b and b>a:
    print("true")
else:
    print("false")'''

#if-elif
'''a=8
b=10
if a==b:
    print("equal")
elif a>b:
    print("greater")
elif a!=b:
    print("not equal")'''

#if-elif-else
'''a=int(input())
b=int(input())
if a<b:
    print("less")
elif a==b:
    print("equal")
else:
    print("none")'''

#multiple if conditions

'''a=4
b=8
if a>b:
    print("greater")
if a==b:
    print("equal")
if b>a:
    print("true")'''

'''a=4
b=8
if a<b:
    print("greater")
if a==b:
    print("equal")
if b>a:
    print("true")'''

'''a=4
b=8
if a>b:
    print("greater")
elif a==b:
    print("equal")
elif b>a:
    print("true")'''

'''a=4
b=8
if a<b:
    print("greater")
if a!=b:
    print("equal")
if b>a:
    print("true")'''

'''a=4
b=8
if a<b:
    print("greater")
elif a!=b:
    print("equal")
elif b>a:
    print("true")'''

#nested-if

'''a=10
b=20
if a>b:
    print("greater")
    if a!=b:
        print("not equal")'''

'''a=10
b=20
if a<b:
    print("greater")
    if a!=b:
        print("not equal")'''

'''a=10
b=20
if a<b:
    print("greater")
    if a==b:
        print("not equal")'''
a=10
b=20
if a>b:
    print("greater")
    if a!=b:
        print("not equal")
else:
    print("false")






    


    
