Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #chr
>>> chr(84)
'T'
>>> chr(65)
'A'
>>> chr(90)
'Z'
>>> chr('a')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    chr('a')
TypeError: 'str' object cannot be interpreted as an integer
>>> ord('a')
97
>>> ord('z')
122
>>> chr(65,90)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    chr(65,90)
TypeError: chr() takes exactly one argument (2 given)
>>> ord('A','Z')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    ord('A','Z')
TypeError: ord() takes exactly one argument (2 given)
>>> import string
>>> def display_characters():
...     for char in string.ascii_uppercase:
...         print(char,end=' ')
... 
...         
>>> 
>>> def display_characters():
...     for char in string.ascii_uppercase:
...         print(char,end=' ')
... display_characters()
SyntaxError: invalid syntax
for i in range(65,91):
    print(chr(i),end=" ")

    
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
for i in range(97,123):
    print(chr(i),end=" ")

    
a b c d e f g h i j k l m n o p q r s t u v w x y z 
for char in string.ascii_uppercase:
    print(chr(char),end=" ")

    
Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    print(chr(char),end=" ")
TypeError: 'str' object cannot be interpreted as an integer
