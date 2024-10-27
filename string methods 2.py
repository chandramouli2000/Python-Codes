Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #.format method
>>> a="motu"
>>> b="patlu"
>>> print("hello",a+b)
hello motupatlu
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> 
... print("hello {} {}".format(a,b))
... 
hello motu patlu
>>> 
... print("hello {} {}".format(a,b))
... 
hello motu patlu
>>> print("hello {} hello {]".format(a,b))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print("hello {} hello {]".format(a,b))
ValueError: expected '}' before end of string
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> 
>>> #f string
>>> a="sita"
>>> b="ram"
>>> print(f"hello {a} {b}")
hello sita ram
>>> print(f"hello {a} hello {b}")
hello sita hello ram
