Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[10,3,4,1,0,5,2,9,7,6]
>>> a1=a[0:5]
>>> a1
[10, 3, 4, 1, 0]
>>> a2=a[5:]
>>> a2
[5, 2, 9, 7, 6]
>>> a1.sort()
>>> a1
[0, 1, 3, 4, 10]
>>> a2.sort()
>>> a2
[2, 5, 6, 7, 9]
>>> a1.reverse()
>>> a1
[10, 4, 3, 1, 0]
>>> a2.reverse()
>>> a2
[9, 7, 6, 5, 2]
>>> b=a1+a2
>>> b
[10, 4, 3, 1, 0, 9, 7, 6, 5, 2]
>>> 
>>> b=["city of destiny "]
>>> b1[0:8]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b1[0:8]
NameError: name 'b1' is not defined. Did you mean: 'a1'?
>>> b1=b[0:8]
>>> b1
['city of destiny ']
>>> 
>>> c="city of destiny"
>>> c1=c[0:8]
>>> c1
'city of '
c2=c[8:]
c2
'destiny'
d=c1+c2
d
'city of destiny'

e="python","java","css"
e.append()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    e.append()
AttributeError: 'tuple' object has no attribute 'append'
