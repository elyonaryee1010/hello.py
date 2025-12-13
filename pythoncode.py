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

#Data Structures in Python -2
my_tuple = ()
print(my_tuple)
my_tuple =(1,2,3)
print(my_tuple)

my_tuple =(1,2,3, "hello")
print("my_tuple")

my_tuple =(1,2,3, "hello", 4.5)
print(my_tuple)

my_tuple =(1,2,3, "hello")
print(my_tuple)
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[5])
print(my_tuple[10])

print(my_tuple[0:3])

##Activity-2
my_set={1,2,2,3,4,4,5,6,6,7,7,8,8,8}
print("my_set", my_set)

my_set.add(10)
print("updated", my_set)

set1=my_set
set2=(10,9,2,56,79)
print("difference is:", set1.difference(set2))

#activity-3
setun1={"purple", "red"}
setun2={"white", "orange"}
print("union", setun1.union(setun2))

## activity-4
setx={"plum", "apple"}
sety={"apple", "grape"}
print("intersection", setx.intersection(sety))


#activity
class Person(object):
    def _init_(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)

class Employee(Person):
    def _init_(self,name,age,empid):
        self.empid = empid
        super()._init_(name, age)

a=Employee("janik", 34, 1001)
a.display()

#activity 2
class Person:
    def _init_(self, fname, lname):
        self.firstname= fname
        self.lname= lname
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def _init_(self, fname, lname, year):
        super()._init_(fname, lname)
        self.graduationyear = year
x=Student("janik", "sinner", 2016)
x.printname()
print(x.graduationyear)


##activity-3
class Parrot:
    species={"bird"}
    def _int_(self, name, age):
        self.name = name
        self.age = age
blue=Parrot("blue", 10)
woo=Parrot("woo", 15)
print("blue is a {}".format(blue._class_.species))
print("woo is a {}".format(woo._class_.species))

#Activity 4

class Parrot:
    species={"bird"}
    def _init_(self, name, age):
        self.name = name
        self.age = age



def sing(self)
    print(f"{self.name} says squawk")
    print(f"{self.name} is a specie of {self.species}")

def dance(self)
    print(f"{self.name} dances")

ames=Parrot("ames", 10)
whu=Parrot("whu", 14)

ames.sing()
whu.dance()

#Constructor and Destructor code
class Employee:
    def_init_(self):
     print("Employer has been created")
    
    def_del_(self):
      print("Destructor called. employee deleted")
obj = Employee()
del obj

#Library

  class Library:
    def __init__(self, name):
        self.name = name
        self.books = ["Harry Potter", "Rich Dad Poor Dad", "Atomic Habits", "Python Basics"]
        self.lend_data = {}  # To track which user has borrowed which book

    def display_books(self):
        print("\n📚 Available Books in the Library:")
        for book in self.books:
            print(f" - {book}")

    def lend_book(self, user, book):
        if book not in self.books:
            print(f"❌ The book '{book}' is not available in the library.")
        elif book in self.lend_data:
            print(f"⚠️ Sorry, '{book}' is currently lent out to {self.lend_data[book]}.")
        else:
            self.lend_data[book] = user
            print(f"✅ Book '{book}' has been lent to {user}.")

    def add_book(self, book):
        if book in self.books:
            print("⚠️ This book already exists in the library.")
        else:
            self.books.append(book)
            print(f"✅ Book '{book}' has been added to the library.")

    def return_book(self, book):
        if book in self.lend_data:
            del self.lend_data[book]
            print(f"✅ Book '{book}' has been returned successfully.")
        else:
            print(f"⚠️ '{book}' was not lent out from this library.")


# --- Main Program ---

if __name__ == "__main__":
    my_library = Library("City Central Library")

    while True:
        print("\n========== Library Menu ==========")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Exit")
        print("===================================")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            my_library.display_books()

        elif choice == '2':
            user = input("Enter your name: ")
            book = input("Enter the book name you want to borrow: ")
            my_library.lend_book(user, book)

        elif choice == '3':
            book = input("Enter the name of the book to add: ")
            my_library.add_book(book)

        elif choice == '4':
            book = input("Enter the name of the book to return: ")
            my_library.return_book(book)

        elif choice == '5':
            print("\n📘 Thank you for using the Library Management System!")
            break

        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")


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

#Data Structures in Python -2
my_tuple = ()
print(my_tuple)
my_tuple =(1,2,3)
print(my_tuple)

my_tuple =(1,2,3, "hello")
print("my_tuple")

my_tuple =(1,2,3, "hello", 4.5)
print(my_tuple)

my_tuple =(1,2,3, "hello")
print(my_tuple)
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[5])
print(my_tuple[10])

print(my_tuple[0:3])

##Activity-2
my_set={1,2,2,3,4,4,5,6,6,7,7,8,8,8}
print("my_set", my_set)

my_set.add(10)
print("updated", my_set)

set1=my_set
set2=(10,9,2,56,79)
print("difference is:", set1.difference(set2))

#activity-3
setun1={"purple", "red"}
setun2={"white", "orange"}
print("union", setun1.union(setun2))

## activity-4
setx={"plum", "apple"}
sety={"apple", "grape"}
print("intersection", setx.intersection(sety))


#activity
class Person(object):
    def _init_(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)

class Employee(Person):
    def _init_(self,name,age,empid):
        self.empid = empid
        super()._init_(name, age)

a=Employee("janik", 34, 1001)
a.display()

#activity 2
class Person:
    def _init_(self, fname, lname):
        self.firstname= fname
        self.lname= lname
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def _init_(self, fname, lname, year):
        super()._init_(fname, lname)
        self.graduationyear = year
x=Student("janik", "sinner", 2016)
x.printname()
print(x.graduationyear)


##activity-3
class Parrot:
    species={"bird"}
    def _int_(self, name, age):
        self.name = name
        self.age = age
blue=Parrot("blue", 10)
woo=Parrot("woo", 15)
print("blue is a {}".format(blue._class_.species))
print("woo is a {}".format(woo._class_.species))

#Activity 4

class Parrot:
    species={"bird"}
    def _init_(self, name, age):
        self.name = name
        self.age = age



def sing(self)
    print(f"{self.name} says squawk")
    print(f"{self.name} is a specie of {self.species}")

def dance(self)
    print(f"{self.name} dances")

ames=Parrot("ames", 10)
whu=Parrot("whu", 14)

ames.sing()
whu.dance()


#Bot assingment

class robot:
    species="computer"
    def __init__(self, name, age):
     self.name = name
     self.age = age
tom=robot("tom", 15)
jerry=robot("jerry", 15)

user_input = input("Ask them their names:")
print(f"Hello my name is Tom and I am a {tom.species}")
print(f"Hello my name is jerry and I am a{tom.species}")

    
#Constructor and Destructor code
class Employee:
    def_init_(self):
       print("Employer has been created")
    
    def_del_(self):
       print("Destructor called. employee deleted")
obj = Employee()
del obj

#Library

class Library:
    def __init__(self, name):
        self.name = name
        self.books = ["Harry Potter", "Rich Dad Poor Dad", "Atomic Habits", "Python Basics"]
        self.lend_data = {}  # To track which user has borrowed which book

    def display_books(self):
        print("\n📚 Available Books in the Library:")
        for book in self.books:
            print(f" - {book}")

    def lend_book(self, user, book):
        if book not in self.books:
            print(f"❌ The book '{book}' is not available in the library.")
        elif book in self.lend_data:
            print(f"⚠️ Sorry, '{book}' is currently lent out to {self.lend_data[book]}.")
        else:
            self.lend_data[book] = user
            print(f"✅ Book '{book}' has been lent to {user}.")

    def add_book(self, book):
        if book in self.books:
            print("⚠️ This book already exists in the library.")
        else:
            self.books.append(book)
            print(f"✅ Book '{book}' has been added to the library.")

    def return_book(self, book):
        if book in self.lend_data:
            del self.lend_data[book]
            print(f"✅ Book '{book}' has been returned successfully.")
        else:
            print(f"⚠️ '{book}' was not lent out from this library.")


# --- Main Program ---

if __name__ == "__main__":
    my_library = Library("City Central Library")

    while True:
        print("\n========== Library Menu ==========")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Exit")
        print("===================================")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            my_library.display_books()

        elif choice == '2':
            user = input("Enter your name: ")
            book = input("Enter the book name you want to borrow: ")
            my_library.lend_book(user, book)

        elif choice == '3':
            book = input("Enter the name of the book to add: ")
            my_library.add_book(book)

        elif choice == '4':
            book = input("Enter the name of the book to return: ")
            my_library.return_book(book)

        elif choice == '5':
            print("\n📘 Thank you for using the Library Management System!")
            break

        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")


            #Inheritance
        class Vehicle:
            def _init_(self, name, max_speed, mileage):
                self.name=name
                self.max_speed=max_speed
                self.mileage=mileage
        class Bus(Vehicle):
                pass

            school_bus=Bus("School Volvo", 50, 300)
            print("Vehicle name:", school_bus.name, "\nSpeed:", school_bus.max_speed,
            "\nMileage:", school_bus.mileage)

            #Activity-2
        class Person(object):
            def _init_(self,name, idnumber):
                self.name=name
                self.idnumber=idnumber
            def display(self):
                print(self.name)
                print(self.idnumber)
        class Employee(Person):
            def _init_(self,name,salary,post)
            self.salary=salary
            self.post=post
            Person._init_(self,name,idnumber)
        a = Employee('Mark', 886012, 20009,"Internal Software")
        a.display()
        

         #Polymorphism

class Cat:
    def _init_(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
        
    def make_sound(self):
        print("Meow")
        
        
class Dog:
    def _init_(self, name, age):
        self.name=name
        self.age=age
        
    def info(self):
        print(f"I am a {self.name}, and I am {self.age} years old")
        
    def make_sound(self):
        print("Bark")
            
cat1 = Cat("Katson", 25)
dog1 = Dog("Dugson", 8)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    
    #Activity-2
    
class Computer:
        
    def _init_(self):
        self._maxprice = 900
            
    def sell(self):
        print("Selling Price:{}".format(self._maxprice))
            
    def setMaxPrice(self, price):
        self._maxprice = price
                
c = Computer()
c.sell()

#change the price
c._maxprice = 1000
c.sell()
    def make_sound(self):
        print()

     





       



 
