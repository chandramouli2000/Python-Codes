
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list[]
>>> a=[3,4.5,"python",7+8j,True,False]
>>> print(a)
[3, 4.5, 'python', (7+8j), True, False]
>>> type(a)
<class 'list'>
>>> b=4
>>> type(b)
<class 'int'>
>>> c=[5,6,7,8]
>>> type(c)
<class 'list'>
>>> 
>>> #append()
>>> a=["python","java","c","c++"]
>>> type(a)
<class 'list'>
>>> a.append("ml")
>>> print(a)
['python', 'java', 'c', 'c++', 'ml']
>>> a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
>>> 
>>> #extend
>>> a=["apple","banana","grapes"]
>>> a.extend("kiwi","mango")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.extend("kiwi","mango")
TypeError: list.extend() takes exactly one argument (2 given)
>>> a.extend(["kiwi","mango"])
>>> print(a)
['apple', 'banana', 'grapes', 'kiwi', 'mango']
>>> 
#insert()
a=["html","css","js"]
a.insert(1,"python")
print(a)
['html', 'python', 'css', 'js']
a.insert(0,"java")
print(a)
['java', 'html', 'python', 'css', 'js']

#copy()
a=["code","codegnan","course"]
a.copy()
['code', 'codegnan', 'course']

#remove()
a.remove("course")
a
['code', 'codegnan']

#pop()
a.pop("code")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.pop("code")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(0)
'code'
a

a
['codegnan']
a.pop()
'codegnan'
a
[]

#sort()
a=["hello","how","are","you"]
a.sort()
a
['are', 'hello', 'how', 'you']
b=[3,2,8,5,9,4,1,6,21,12]
b.sort()
b
[1, 2, 3, 4, 5, 6, 8, 9, 12, 21]

#reverse()
a.reverse()
a
['you', 'how', 'hello', 'are']
b.reverse()
b
[21, 12, 9, 8, 6, 5, 4, 3, 2, 1]
c=[30,10,20,40,5]
c.sort(reverse=True)
c
[40, 30, 20, 10, 5]
c.sort(reverse=False)
c
[5, 10, 20, 30, 40]

#index
a=["python","java","css"]
a.index(2)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a.index(2)
ValueError: 2 is not in list
a.index("css")
2

b="python"
len(b)
6
c=["python"]
len(c)
1

#count()
a=["java","c","c++","python","css"]
a.count("java")
1
a,counr("c++")
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a,counr("c++")
NameError: name 'counr' is not defined. Did you mean: 'round'?
a.count("c++")
1


