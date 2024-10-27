Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[:7:2]
'dt c'
>>> a[::3]
'dacn'
>>> 
>>> 
>>> b="cloud computing"
>>> b[::6]
'cci'
>>> b[::5]
'c u'
>>> b[::3]
'cucpi'
>>> b[::7]
'cog'
>>> b[5:9]
' com'
>>> b[:6]
'cloud '
>>> b[8:]
'mputing'
>>> b[2:8]
'oud co'
>>> 
>>> 
>>> c="python course"
>>> c[1:5:2]
'yh'
>>> c[2:8:2]
'to '
>>> c[3:11:1]
'hon cour'
c[5:12:3]
'nos'
c[1:10:4]
'ynu'

e="hello python"
e[-1:-6:-2]
'nhy'
e[-2:-9:-4]
'op'
e[-4:-12:-5]
'tl'
e[-3:-9:-2]
'hy '
