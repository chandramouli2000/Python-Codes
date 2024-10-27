#1)Write a program to find whether a given year is a leap year or not satisfying all the possible condition for a leap year?
'''while True:
    def leapyear(year): 
        if ((year%4==0) and (year%100!=0) or (year%400==0)):
            print(" Its leap year")
        else:
            print("Its not a leap year")

    year=int(input("Enter a number:"))
    leapyear(year)'''


#2) Write a program to Convert temperature entered in Fahrenheit to Celsius ?

#Hint: The conversion formula is Celsius = (F-32) / 1.8

'''def fahrenheit():
    F=int(input("Enter the Fahrenheit Tempearture :"))
    celsius = (F-32)  / 1.8
    print("Temperature in Celsius ",round(celsius,3)) 
fahrenheit()'''


#3) Write a program to calculate factorial of a number by accepting input from the user?

'''num=int(input("Enter the Factorial of a number :"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
    print(f"The factorial of {num} is :{factorial}")'''

#4)Write a program to calculate the sum and average of First n natural numbers by taking n as input from the user?

'''n=int(input("The First n natural numbers : "))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
print("sum of first ",n,"number is:",sum)
average=sum/n
print("Average of ",n,"number is:",average)'''

#5)Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 1 and 200 (both included).

#The numbers obtained should be printed in a comma-separated sequence on a single line along with the total number count.

'''result=[]
for i in range(1,201):
    if i %7==0 and i %5 !=0:
        result.append(str(i))
result_str=",".join(result)
count=len(result)
print(result_str)
print("Count:",count)'''

#6)Write a program to find the sum of squares of first 20 Odd numbers?

'''sum_of_squares=0
for i in range(20):
    odd_numbers= 2*i+1
    sum_of_squares += odd_numbers **2
print("The sum of squares of first 20 odd numbers is:",sum_of_squares)'''


#7)Write a program that accepts a sentence and calculate the number of letters and digits.

#Suppose the following input is supplied to the program:
#hello Codegnan! 243
#Then, the output should be:
#LETTERS 13
#DIGITS 3

'''def count_letters_and_digits(sentence):
    letters_count=0
    digits_count=0
    for i in sentence:
        if i.isalpha():
            letters_count +=1
        elif i.isdigit():
            digits_count += 1
    print(f"lETTERS {letters_count}")
    print(f"DIGITS {digits_count}")
a="hello Codegnan ! 243"
count_letters_and_digits(a)'''

#8)write a program to print the multiplication table of n,by taking n as input from user

'''def multiplication_table(n):
    for i in range(1,21):
        print(f"{n} x {i} = {n*i}")
n=int(input("Enter the number: "))
multiplication_table(n)'''

#9)Write a program to calculate the area of the triangle by accepting base and height as integer/float input from the user?

'''def area_of_the_triangle(base,height):
    return 0.5 * base * height
base=float(input("Enter the base of the triangle:"))
height=float(input("Enter the height of the triangle:"))
area=area_of_the_triangle(base,height)
print(f"The Area of the triangle is:{area}")'''

#10)Write a program to find the greatest number from three numbers by accepting three integer inputs from the user?

'''def greatest(num1,num2,num3):
    return max(num1,num2,num3)
num1= int(input("Enter the first number:"))
num2= int(input("Enter the second number:"))
num3= int(input("Enter the third number:"))
num=greatest(num1,num2,num3)
print(f"The greatest number is:{num}")'''

#11)Write a program that prompts the user to enter a number between 1-7 and then displays the corresponding day of the week







    
