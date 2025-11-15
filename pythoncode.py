#This is a python file

'''
This is a multi line comments

'''

print("hello")
print("Sum of 3 and 4 is : ",3+4)
print("Product of 3 and 4 is : ",3*4)

#New code penguin
name = "Penguin"
age = 15
is_student = True

print("Name :", name)
print("Data Type of Name is", type(name))
print("Age :", age)
print("Data Type of Age is", type(age))
print("is_student :", is_student)
print("Data type of is_student is", type(is_student))
print("Weight :", weight)
print("Data Type of weight is", type(weight))

print("/n After Type Casting...")
age = str(age)
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of Weight is", type(weight))

num1 = 45
num2 = 3

print("Number 1", num1)
print("Number 2", num2)
print("Addition: ", num1+num2)
print("Product: ", num1*num2)
print("Division :", num1/num2)
print("Floor Division:", num1//num2)
print("Modulus Operation :", num1%num2)
print("Square :", num2**2)
print("Square Root :", num1**0.5)
print("Equal ?", num1==num2)
print("Number 1 greater?", num1>num2)
print("Number 2 greater?", num1<num2
print("Not equal ?", num1!=num2)


result = num1/2+num2**2+10
print("RESULT OF GIVEN EQUATION IS:", result)


first_name = "Codingal"
last_name = "Educations"
full_name = first_name+last_name
example = "Haa"*3


print("First Name:", first_name)
print("Last Name:", last_name)
print("String Multiplied 5 times gives this result :", example)


word = 'Coding'
print("Length of String :", len(word))
print("First Letter of String :", word[0])
print("Last Letter of String :", word[5])
print("String Sliced :", word[0:3])


#Take Input Val from user

x = input("Enter X's value")
y = input("Enter Y's value")

#Swapping
temp = x
x = y
y = temp

#Displaying results after swapping
print("Value of x after swapping", x)
print("Value of y after swapping", y)




    
    

#Odd or Even

number = int(input("Enter a numer :"))
print("number is :", number)
    if number%2==0:
        print("Even Number detected")
        else:
            print("Odd Number detected")

            #BMI
weight = int(input("Enter your weight in kilograms :"))
height = int(input("Enter your weight in cm"))
BMI = eight/(height/100)**2
print("Your BMI is :", BMI)

if BMI<18.5:
     print("Your are underweight")
elif BMI>=18.5 and BMI<24.9:
    print("You are normal")
elif BMI>=25 and BMI<29.9:
    print("You are overweight")
else:
    print("You're obese")

    #Double Check

number = int(input("Enter your number here"))
print("You're number is:", number)
if number>=50:
    if num%2==0
    print("Great")
else:
    print("Less")

    else:
        print("nothing_)"


    #Time &date
import datetime
current_time = datetie.datime.new()
print("current time here is:", current_time)

    
    

#Activity 15/11/25
for i in range(1,6):
  print(f"23* {i} = {23* i}")

  #Activity-2
n= int(input("Enter the number of rows"))
for i in range(1,n+1):
     for j in range(i):
      print('#',end="")
    print()

    #Activity 3
    total_sum = sum(range(1,21))
    print("t he best for sum of first ten natural numbers is:", total_sum")

    #Activity-4
    num= int(input("Enter a number:"))
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                print(f"{num} is not a prime number")
                break
            else:
                print(f"{num} is a prime number")
         


