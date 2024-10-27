#loops
#for,while,range,break,continue,pass

#for loop
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=4,5,6,7,8
for i in a:
    print(i,end=" ")'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(i))
    print(type(a))'''

'''a=(4,5,6,7,8)
for i in a:
    print(i)
    print(type(i))
    print(type(a))'''

'''a={5,3,9,2,1,0}
for i in a:
    print(i)
    print(type(a))'''

'''a={"name":"mouli","place":"vizag"}
for i in a:
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)'''

'''a="apple","banana","grapes"
for i in a:
    print(i,end=" ")
    print(type(i))
    print(type(a))'''

#while loop

'''a=10
while a>1:
    print(a)'''

'''a=10
while a>1:
    print(a)
    a=a-1'''
#voting
'''while True:
    age=int(input("enter the age"))
    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")'''

#range()
#start-stop-step

'''for i in range(10):
    print(i)'''

'''for i in range(5,15):
    print(i)'''

'''for i in range(0,50,5):
    print(i)'''

'''for i in range(2,20,2):
    print(i)'''

'''for i in range(0,30,3):
    print(i)'''

#break
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''

#continue

'''a=20
while a>2:
    print(a)
    a=a-1
    if a==7:
        continue'''
'''a=20
while a>2:
    a=a-1
    if a==7:
        continue
    print(a)'''
'''a=5
while a>1:
    a=a-1
    if a==4:
        continue
    print(a)'''

'''a=20
while a>2:
    a=a-1
    if a==7:
        break
    print(a)'''

'''for i in range(10):
    if i==4:
        continue
    print(i)'''

'''for i in range(10):
    if i==4:
        break
    print(i)'''

#pass
'''a="codegnan"
for i in a:
    if i=="g":
        pass
    else:
        print(i)'''

'''a="codegnan"
for i in a:
    if i=="g":
        pass
    print(i)'''

'''a=2,3,4,5,7
for i in a:
    if i==10:
        pass
    else:
        print(i)'''

'''a=2,3,4,5,7
for i in a:
    if i==7:
        pass
    else:
        print(i)'''


a=["python","codegnan","course"]
'''b=str(a)
print(b.upper())'''

for i in a:
    print(i.upper(),end=" ")


