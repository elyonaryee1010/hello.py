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



        



 
