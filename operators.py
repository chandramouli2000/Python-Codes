Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#assignment opeartor
print(4+5)
9
a=4
b=6
a+=b
a
10
a-=2
a
8
a*=3
a
24
a//=2
a
12
a/=2
a
6.0
a%=3
a
0.0
a**=2
a
0.0

#comparision operator
a=5
b=10
a<b
True
b>a
True
a<=b
True
b>=a
True
a>=b
False
b<=a
False
a==b
False
a!=b
True
a=2
b=2
a==b
True

#logical
a=8
b=9
a==b and a!=b
False
a!=b and a<b
True
a<b or b>a
True
a!=b or a==b
True
a<=b or b>=a
True
a<b not b>a
SyntaxError: invalid syntax
not True
False
not False
True

#identify operators
a=4.5
it type(a) is float:
    
SyntaxError: invalid syntax
a=4.5
if type(a) is float:
    print("it is float")
else:
    print("it is not float")

    
it is float
if type(a) is not float:
    print("true")
else:
    print("false")

    
false

#membership
a=10,20,30,40,50
if 10 in a:
    print(10)

10
if 100 in a:
    print(100)

...     
>>> if 40 in a:
...     print(40)
... 
...     
40
>>> if 50 not in a:
...     print(50)
... 
...     
>>> 
>>> if 80 not in a:
...     print(80)
... 
...     
80
>>> a=2,3,4,5,6,7
>>> if 2 in a:
...     print(2)
... else;
SyntaxError: expected ':'
>>> else:
...     
SyntaxError: invalid syntax
>>> a=2,3,4,5,6,7
>>> if 2 in a:
...     print(2)
... else:
...     print("true")
... 
...     
2
>>> if 8 in a:
...     print(8)
... else:
...     print("true")
... 
...     
true
