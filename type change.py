Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> b=set(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    b=set(a)
TypeError: 'int' object is not iterable
>>> b=str(a)
>>> b
'10'
>>> type(b)
<class 'str'>
>>> a=[1,2,3,4,5]
>>> type(a)
<class 'list'>
>>> b=set(a)
>>> b
{1, 2, 3, 4, 5}
>>> type(b)
<class 'set'>
>>> c=tuple(b)
>>> c
(1, 2, 3, 4, 5)
>>> type(c)
<class 'tuple'>
