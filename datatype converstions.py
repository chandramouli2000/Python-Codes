Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #datatypes conversations
>>> int(2)
2
>>> int(2.3)
2
>>> int("mouli")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("mouli")
ValueError: invalid literal for int() with base 10: 'mouli'
>>> int(2+6j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(2+6j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> 
>>> float(4)
4.0
>>> float(4.3)
4.3
>>> flaot("chandra")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    flaot("chandra")
NameError: name 'flaot' is not defined. Did you mean: 'float'?
>>> float("chandra")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("chandra")
ValueError: could not convert string to float: 'chandra'
>>> float(2+6j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(2+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> 
>>> str(3)
'3'
str(3.5)
'3.5'
str("mouli")
'mouli'
str(6i+4)
SyntaxError: invalid decimal literal
str(4+6j)
'(4+6j)'
str(True)
'True'
str(False)
'False'

complex(4)
(4+0j)
complex(3.6)
(3.6+0j)
complex("python")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    complex("python")
ValueError: complex() arg is a malformed string
complex(2+7j)
(2+7j)
complex(True)
(1+0j)
complex(False)
0j

bool(4)
True
bool(7.3)
True
bool('mouli')
True
bool(7j+4)
True
bool(1)
True
bool(0)
False
