Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#tuple()
a=(2,5.6,"python",7+8j,True,False)
print(a)
(2, 5.6, 'python', (7+8j), True, False)
type(a)
<class 'tuple'>
#len()
len(a)
6
#count
a.count(5.6)
1
#index
a.index(7+8j)
3
a.count("python")
1
a.count(True)
1

b=(1,2,3,4,5,6)
b.count(4)
1
b.count(2)
1
b.count(5)
1
\
a.count(False)
1
c=(1,1,2,2,2)
c.count(2)
3


#set{}
a={5,8.9,"mouli",3+9j,True,False}
print(a)
{False, True, 'mouli', 5, 8.9, (3+9j)}
type(a)
<class 'set'>
b={7,9,0,1,5}
print(b)
{0, 1, 5, 7, 9}
type(b)
<class 'set'>


#add()
a={3,6,8,2,1,4}
a.add(20)
a
{1, 2, 3, 4, 20, 6, 8}
#issubset()
a={1,2,3,4,5}
b={3,4,5}
a.issubset()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.issubset()
TypeError: set.issubset() takes exactly one argument (0 given)
a.issubset(b)
False
b.issubset(a)
True

c={1,3,5,6,7,8}
#issuperset()
a={1,3,5,6,7,8}
b={7,8,9}
a.issuperset(b)
False
b.issuperset(a)
False
a={1,2,3,4,5,6}
b={5,6}
a.issuperset(b)
True

#union()
a={1,2,3,4,5,6}
b={6,7,8,9,10}
a.unoin(b)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.unoin(b)
AttributeError: 'set' object has no attribute 'unoin'. Did you mean: 'union'?
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#intersection()
a={4,5,6,7,8}
b={6,7}
a.intersection(b)
{6, 7}
b.intersection(a)
{6, 7}

#update()
a={2,3,4,5,6}
b={6,7,8,9}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8, 9}
a
{2, 3, 4, 5, 6, 7, 8, 9}

b
{8, 9, 6, 7}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9}

#symmetric
#differnce()
a={6,7,8,9,10}
b={8,9,10,11,12}
a.difference(b)
{6, 7}
b.difference(a)
{11, 12}

a={2,4,6,8,10}
b={3,4,5,6,12}
a.symmetric_difference(b)
{2, 3, 5, 8, 10, 12}

a={4,5,6,7,8}
b={6,7,8,9,10}
a.difference_update(a)
a
set()
#difference_update()
a={4,5,6,8,10}
b={6,7,8,9,10}
a.difference_update(b)
a
{4, 5}
a
{4, 5}
b.difference_update(a)
b
{6, 7, 8, 9, 10}
b
{6, 7, 8, 9, 10}

#Symmetric_difference_update()
a={9,8,7,6,5}
b={1,2,3,5,6,8}
a.symmetric_difference_update(b)
a
{1, 2, 3, 7, 9}
a
{1, 2, 3, 7, 9}
b.symmetric_difference_update(a)
b
{5, 6, 7, 8, 9}
b
{5, 6, 7, 8, 9}
>>> 
>>> #pop()
>>> a={1,2,3,4,5,6,7}
>>> b={6,7,8,9,10}
>>> a.pop()
1
>>> a
{2, 3, 4, 5, 6, 7}
>>> #remove()
>>> a.remove(5)
>>> a
{2, 3, 4, 6, 7}
>>> #discard()
>>> a={1,2,3,4,5}
>>> b={4,5,6,7,8}
>>> a.discard(1)
>>> a
{2, 3, 4, 5}
>>> a.copy()
{2, 3, 4, 5}
>>> #clear()
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(20)
>>> b
{20}
>>> 
>>> #disjoint()
>>> a={3,5,7,9,11,15}
>>> b={2,4,6,8,10,15,20}
>>> a.isdisjoint(b)
False
>>> a={3,4,5,6}
>>> b={7,8,9,10}
>>> a.isdisjoint(b)
True
