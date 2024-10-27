Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b=10
>>> a=b
>>> print(a)
10
>>> a,b=b,a
>>> print(a,b)
10 10
>>> a=b;b=a
>>> print(a,b)
10 10
>>> 
>>> a=5
>>> b=10
>>> t
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t
NameError: name 't' is not defined
>>> a=5
>>> b=10
>>> temp
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    temp
NameError: name 'temp' is not defined
>>> a=5
>>> b=10
>>> a,b=b,a
>>> print("a=",a)
a= 10
>>> print("b=",b)
b= 5
