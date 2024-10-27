#Modules

'''if __name__=="__main__":
    a=[1,2,3,4,5,6,7]
    #a.append("code")
    a.extend("code")
    print(a)'''

'''def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()'''

#math  module
'''import math
print(math.pi)
print(math.pi*2)
print(math.sqrt(2))
print(math.log(10))
print(math.log(1))
print(math.sin(390))
print(math.cos(60))
print(math.tan(90))
print(math.ceil(7))'''

'''import math
print(math.pi)
from math import pi,sqrt
print(pi)
print(sqrt(2))'''

#random module

'''import random
a=random.sample(range(20,40),15)
print(a)'''

'''import random
a=random.randint(7,15)
print(a)'''

'''import random
a=[10,20,30,40,50]
b=random.choice(a)
print(b)'''

'''import random
a=[10,20,30,40,50]
b=random.choices(a)
print(a)'''


#task Dice code

'''import random
while True:
    input("Enter the roll of Dice:")
    b=random.randint(10,30)
    print(b)
    c=input("Choose the option -> (yes/no)")
    if c=="yes":
       continue
    elif c=="no":
        break
    else:
        print("invaild option")'''


#calendar module

'''import calendar
year=2024
month=10
print(calendar.month(year,month))'''

'''import calendar
year=2024
for i in range(1,13):
    print(calendar.month(year,i))'''

'''import calendar
year=2025
print(calendar.calendar(year))'''

'''import calendar
year=int(input("Enter a year:"))
month=int(input("enter a month:"))
print(calendar.month(year,month))'''


#date & time module

'''from datetime import date
a=date.today()
print(a)'''

'''from datetime import datetime
a=datetime.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()'''

'''from datetime import datetime
a=datetime.now().time()
print(a)'''

'''import time
a=time.time()
print(a) #epoch time

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"today time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")
print(f"Day is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''


'''import time
import random
for i in range(10):
    a=random.randint(1000,2000)
    print(a)
    time.sleep(3)'''

#regex -> regular expressions

'''a="codegnan is in vijayawada"
print(a)

b="codegnan\nis\tin\nvijayawada"
print(b)

#raw string
c=r"codegnan\nis\nin\tvijayawada"
print(c)'''

    
#compile(),search(),findall(),split(),sub()

#sequence characters:

#1) : \w->it matches alphanumeric
#2) : \W->it matches non-alphanumeric
#3) : \d->matches any digit
#4) : \D->matches non digit
#5) : \s->represents white spaces
#6) : \S->represents non white spaces

#compile()
import re
a="mat map code cash codegnan math money cat cap"
'''b=re.compile(r"m\w\w")
print(b)'''

#search()
'''c=b.search(a)
print(c)'''

'''d=re.search(r"m\w+",a)
print(d)'''

#findall()

'''e=re.findall(r"m\w+",a)
print(e)
print(*e)

e=re.findall(r"c\w+",a)
print(e)
print(*e)'''

#split()
'''f=re.split(r"c\w+",a)
print(f)

c=re.split(r"c",a)
print(c)

b=re.split(r"\s",a)
print(b)

d=re.split(r"\S",a)
print(d)'''


#sub()
'''e=re.sub(r"t","k",a)
print(e)'''


b="year 2024 month 10 day 25"
c=re.search(r"\d+",b)
e=re.findall(r"\d+",b)
print(c)
print(e)

f=re.search(r"\D+",b)
d=re.findall(r"\D+",b)
print(f)
print(d)








        
      

