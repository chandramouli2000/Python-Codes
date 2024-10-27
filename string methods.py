Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#string methods
len()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    len()
TypeError: len() takes exactly one argument (0 given)
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=" "
len(c)
1
d=""
len(d)
0


#count
e="twinkle twinkle little star"
cont("twinkle")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    cont("twinkle")
NameError: name 'cont' is not defined
e.count("twinkle")
2
e.count("t")
5
e.count(" ")
3

#find a string
a="code"
a[1]
'o'
a.find("e")
3
b="codegnan"
b.find("n")
5

#escape sequences
#\n->new line
#\t->tabspace
a="name\nmoblieno\tmailid\naddress"
print(a)
name
moblieno	mailid
address
b="name : mouli\nmoblie no : 6304310647\nmail id : mouli@gamil.com"
print(b)
name : mouli
moblie no : 6304310647
mail id : mouli@gamil.com

#replace
a="wait untill you succeed"
a.replace("wait","work")
'work untill you succeed'
b="wait wait untill you succeed"
b.replace("wait","work")
'work work untill you succeed'
b.replace("wait","work",1)
'work wait untill you succeed'


#upper()
a="hello"
a.upper()
'HELLO'

#lower()
b="MOULI"
b.lower()
'mouli'

c="hello world"
c.captialize()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    c.captialize()
AttributeError: 'str' object has no attribute 'captialize'. Did you mean: 'capitalize'?
c.capitalize()
'Hello world'
#title
c.title()
'Hello World'
d="i am in class"
d.title()
'I Am In Class'
d.capitalize()
'I am in class'

a="data science"
a.isupper()
False
a.islower()
True
a.isalpha()
False
b="datascience"
b.isalpha()
True
b.isdigit()
False
b.startswith()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    b.startswith()
TypeError: startswith() takes at least 1 argument (0 given)
b.startswith("d")
True
b.endswith("e")
True


#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="vizag is a city of destiny"
b.split()
['vizag', 'is', 'a', 'city', 'of', 'destiny']

#join()
a="hello","hi","how"
"".join(a)
'hellohihow'
" ".join(a)
'hello hi how'
"z".join(a)
'hellozhizhow'
b="hello"
"z".join(b)
'hzezlzlzo'
"k".join(a)
'hellokhikhow'
c="python "
"f".join(c)
'pfyftfhfofnf '


#strip
#lstrip
>>> #rstrip()
>>> a="         hi        "
>>> a.strip()
'hi'
>>> a.lstrip()
'hi        '
>>> a.rstrip()
'         hi'
>>> 
>>> #formatting
>>> a=10
>>> b=20
>>> print(a+b)
30
>>> print("the sum is",a+b)
the sum is 30
>>> print("the sum is,a+b")
the sum is,a+b
>>> 
>>> c="john"
>>> d="henry"
>>> print("hello",a+b)
hello 30
>>> print("hello",c+d)
hello johnhenry
>>> print("hello",c+" hello "+d)
hello john hello henry
>>> 
>>> #concatenation
>>> a="chandra"
>>> b="ch"
>>> print(a+b)
chandrach
>>> print(a+" "+b)
chandra ch
>>> print(a.title()+" "+b.title())
Chandra Ch
>>> print((a+" "+b).title())
Chandra Ch


