Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> #[7,6,4,3,0,9,8,5,2,1]
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[5:]
>>> a2
[4, 6, 3, 7, 0]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> c=a2+a1
>>> c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
