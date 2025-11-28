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
         

### New Activity

def intro(name):
    print("Hi, I am" + name + "I am red. and this")

user_name=input("Enter your name:")
intro(user_name)

#Activity-2
def recr_factorial(n):
    if n==1:
     return n
    else:
      return n*recr_factorial(n-1)
   num= int(input("Enter a number:"))
    if num<0:
        print("Sorry negative numbers can be used")
        print("Try using positive numbers")
    elif num==0:
       print("Factorial of 0 is 1")
    else:
        print("The Factorial of", num, "is", recr_factorial(num))


#Activity-3
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b)
    return a*b
def div(a,b)
      return a/b

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number:"))
print("Addition:", add(num1,num2))
print("Subtract:", sub(num1,num2))
print("Multiply:", mul(num1,num2))
print("Division:", div(num1,num2))
print("Thank you for using the calculator")


#Activity-1
import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
num_sides = 6
side_length = 70
angle = 360.0/(num_sides)
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()

#Activity-2
turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()
board.forward(100)

board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

board.penup()
board.right(90)
board.forward(100)

board.right(12)
board.forward(100)
board.right(120)
#board.forward(100)

#turtle.done()


##Activity-3
#my_wn = turtle.Screen()
#my_wn.bgcolor("lightgreen")
#my_wn.title("Hello.")
#my_pen = turtle.Turtle()
#size=0
#while True:
    #for i in range(4):
        #my_pen.fd(size+1)
        #my_pen.left(90)
        #size= size-5
        #size= size+1
    

#Python Data class
lst= ['apple', 'banana', 'cherry']
print('The original list is:', lst)
print('Length of the list:', len(lst))

print('The first element of the list:', lst[0])
print('The last element of the list:', lst[5])
print('The first element of the list:', lst[-1])

lst.append('kiwi')
print('The list after appending kiwi is:', lst)

lst.remove('fig')
print('The list after appending fig is:', lst)

lst.sort()
print('The list after appending kiwi is:', lst)

lst.reverse()
print('The list after appending kiwi is:', lst)

lst.clear()
print('The list after appending kiwi is:', lst)
print(lst)

# # Activity2
my_dict={
    'name': 'John',
    'age': '16',
    'city': 'Camden',
    'email': 'John@exple.com',
}


print('the original dictionary is:', my_dict)
print('the original dictionary is:', my_dict['name'])
print('the original dictionary is:', my_dict['age'])

my_dict['state'] = 'New York'
print('the original dictionary is:', my_dict)

## Activity-3
def test(lst1):
    result={}
    for item in lst1:
        result[item[0]]=item[1:]
    return result
    
student_list= [('John', 25,'York'), ('Jane', 30, 'Los Angeles'), ('Jack', 28, 'Boston')]

print(test(student_list))
print("\nOriginal list of list:", student_list)
print("Convert the said list of lists to a dictionary:", student_list)





