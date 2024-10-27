Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dict{}
>>> a={"name":"mouli","place":"vja"}
>>> print(a)
{'name': 'mouli', 'place': 'vja'}
>>> type(a)
<class 'dict'>
>>> #accessing item
>>> a["name"]
'mouli'
>>> 
>>> #keys()
>>> a={"year":2024,"month":9,"day":"tuesday"}
>>> a.keys()
dict_keys(['year', 'month', 'day'])
>>> #values
>>> a.values()
dict_values([2024, 9, 'tuesday'])
>>> #items()
>>> a.items()
dict_items([('year', 2024), ('month', 9), ('day', 'tuesday')])
>>> 
>>> #update
>>> a={"fruit":"apple","colour":"black"}
>>> a.update({"food":"biryani"})
>>> a
{'fruit': 'apple', 'colour': 'black', 'food': 'biryani'}
>>> a.update({"mobile":"android"},{"laptop":"mac"})
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.update({"mobile":"android"},{"laptop":"mac"})
TypeError: update expected at most 1 argument, got 2
>>> a.update({"mobile":"android","laptop":"mac"})
>>> a
{'fruit': 'apple', 'colour': 'black', 'food': 'biryani', 'mobile': 'android', 'laptop': 'mac'}

#setdefault()
a={"country":"india":"city":"vijayawada"}
SyntaxError: invalid syntax
a.setdault("")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.setdault("")
AttributeError: 'dict' object has no attribute 'setdault'. Did you mean: 'setdefault'?
a={"country":"india","city":"vijayawada"}
a.setdefault("year":2024)
SyntaxError: invalid syntax
a.setdefault("year",2024)
2024
a
{'country': 'india', 'city': 'vijayawada', 'year': 2024}
a.copy()
{'country': 'india', 'city': 'vijayawada', 'year': 2024}


#pop()
a={"course":"python","year":2024,"month":"sep"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop(1)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.pop(1)
KeyError: 1
a.pop("year")
2024

#popitem()
a={"name":"pooja","course":"python"}
a.popitem()
('course', 'python')
a
{'name': 'pooja'}

#get()
a.get()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.get()
TypeError: get expected at least 1 argument, got 0
a.get("name")
'pooja'
a
{'name': 'pooja'}

b={"name":"mouli","year":2024}
b.clear()
b
{}

c={"names":"mouli","humble","cute"}
SyntaxError: ':' expected after dictionary key
c={"names":["mouli","humble","cute"],"places":["vja","hyd","vzg"]}
print(a)
{'name': 'pooja'}
print(c)
{'names': ['mouli', 'humble', 'cute'], 'places': ['vja', 'hyd', 'vzg']}
type(c)
<class 'dict'>
a.keys()
dict_keys(['name'])
c.keys()
dict_keys(['names', 'places'])
c.values()
dict_values([['mouli', 'humble', 'cute'], ['vja', 'hyd', 'vzg']])
