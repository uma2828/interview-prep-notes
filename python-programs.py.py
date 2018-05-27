#swap code
x, y = 10, 20   
print (x, y)     
x, y = y, x   
print (x, y)


#increment
x = 10
x += 1
print(x) ## prints 11


#decrement
x = 10
x -= 1
print(x)

 
#type conversion
>>> float(42)  # convert 42 to float
42.0
>>>
>>> float("3.4")  # convert "3.4" to float
3.4
>>>
str() function #
>>>
>>> str(12)   # convert 12 to str
'12'
>>>
>>> str(3.4)  # convert 3.4 to str
'3.4'
>>

#break line
result = 1111100 + 45 - (88 / 43) + 783 \
         + 10 - 33 * 1000 + \
         88 + 3772

print(result)

print("first line\
 second line\
 third line")
 
 
#bool type
>>> bool("")    # an empty string is falsy value
False
>>>
>>> bool(12)    # int 12 is a truthy value
True
>>>
>>> bool(0)     # int 0 is falsy a value
False
>>>
>>> bool([])    # an empty list is a falsy value
False
>>>
>>> bool(())    # an empty tuple is a falsy value
False
>>>
>>> bool(0.2)   # float 0.2 is truthy a value
True
>>>
>>> bool("boolean")   # string "boolean" is a truthy value
True
>>>

True
>>>
>>> 90 > 450     # Is 90 is greater than 450 ? No
False
>>>
>>> 10 <= 11     # Is 10 is smaller than or equal to 11 ? Yes
True
>>>
>>> 31 >= 40     # Is 31 is greater than or equal to 40 ? No
False
>>>
>>> 100 != 101     # Is 100 is not equal to 101 ?  Yes
True
>>>
>>> 50 == 50     # Is 50 is equal to 50 ? Yes
True
>>>
>>>
>>> (10>3) and (15>6)  # both conditions are true so, the result is true
True
>>>
>>> (1>5) and (43==6)  # both conditions are false so, the result is false
False
>>>
>>> (1==1) and (2!=2)  # one condition is false(right operand) so, the result is false
False
>>>


#Membership Operators - in and not in #
The in or not in operators are used to check the existence of a string inside another string. For example:


>>> s1 = "object oriented"
>>>
>>> "ted" in s1    # Does "ted" exists in s1 ?
True
>>>
>>>
>>> "eject" in s1   # Does "eject" exists in s1 ?
False
>>>
>>>
>>> "orion" not in s1   # Doesn't "orion" exists in s1 ?
True
>>>
>>> "en" not in s1   # Doesn't "en" exists in s1 ?
False
print(s1)
String in single quotes
>>> print(s2)
String in double quotes
>>>

#strcat
s1 = "This is " + "one complete string"
>>> print(s1)
This is one complete string
>>>
>>> s2 = "One " + "really really " + "long string"
>>> print(s2)
One really really long string

>>>
>>> s = str(100)
>>> s
'100'
>>> type(s)
<class 'str'>
>>>
>>>
>>> s = "Python" + str(101)
>>> s
'Python101'
>>>

##object.method_name()
Here is an example:

The str class provides methods like upper() and lower() which returns a string after converting it to uppercase and lowercase respectively.

>>>
>>> s1 = "A String"
>>>
>>> s2 = s.lower()
>>> s2
'a string'
>>>
>>> s3 = s.upper()
>>> s3
'A STRING'
>>>
>>> s3
>>>

>>>
>>> "tree" == "tree" 
True
>>>
>>> "pass" != "password"
True
>>>
>>> "@@@" <= "123"
False
>>>
>>> "" <= "123"
True
>>>


#prg for radius and circumferance
radius = int(input("Enter radius: "))
if radius >= 0:
    print("Circumference = ", 2 * 3.14 * radius)
    print("Area = ", 3.14 * radius ** 2 )
else:
    print("Please enter a positive number")
	
#prg to check password	
password = input("Enter a password: ")
if password == "sshh":
    print("Welcome to the Secret World")
else:
    print("You are not allowed here")
	
	gre_score = int(input("Enter your GRE score: "))
per_grad = int(input("Enter percent secured in graduation: "))

if per_grad > 70:
    if gre_score > 150:
        print("Congratulations you are eligible for loan.")
    else:
        print("Your GRE score is no good enough. You should retake the exam.")
else:
    print("Sorry, you are not eligible for loan.")
	
	score = int(input("Enter your marks: "))

	
#using elif	
if score >= 90:
    print("Excellent! Your grade is A")
elif score >= 80:
    print("Great! Your grade is B")
elif score >= 70:
    print("Good! Your grade is C")
elif score >= 60:
    print("Your grade is D. You should work hard on you studies.")
else:
    print("You failed in the exam")

#loops in phyton	
	i = 1
while i <= 100:
    print("Today is Sunday")
    i += 1
	
	
#python101/Chapter-10/sum_from_0_to_10.py
i = 1
sum = 0
while i < 11:
    sum += i    # same as sum = sum + i
    i += 1  

print("sum is", sum)   # print the sum


#for loop which iterates through the elements in a list

>>>
>>> for i in [11, 44, 77, 33, 199]:
...     print(i)
...
11
44
77
33
199
>>>


##for loop which iterates through the characters in a string
>>> for i in "astro":
...    print(i)
...
a
s
t
r
o
>>>

##square
print("Number\t | Square")
print("--------------------")

#break
for num in range(1, 21):
    print(num, "\t\t | ", num*num)
	
	for i in range(1, 10):
    if i == 5:  # when i is 5 exit the loop
        break
    print("i =", i)

print("break out")


#prime no
num = int(input("Enter a number: "))

is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False  # number is not prime
        break  # exit from for loop

if is_prime:
    print(num, "is prime")
else:
    print(num, "is not a prime")
	
#continue
for i in range(1, 10):
    if i % 2 != 0:
        continue
    print("i =", i)
	
##Lists are Mutable #
List are mutable, what this means is that we can modify a list without creating a new list in the process. Consider the following example:

>>>
>>> list1 = ["str", "list", "int", "float"]
>>>
>>> id(list1)   # address where list1 is stored
43223176
>>>
>>> list1[0] = "string"  # Update element at index 0
>>>
>>> list1   # list1 is changed now
['string', 'list', 'int', 'float']
>>>
>>> id(list1)  # notice that the id is still same
43223176
>>>
>>>

##List Concatenation #
List can be joined too using + operator. When operands on both side are lists + operator creates a new list by combing elements from both the lists. For example:

>>>
>>> list1 = [1,2,3]  # create list1
>>> list2 = [11,22,33]  # create list2
>>>
>>> id(list1)   # address of list1
43223112 
>>> id(list2)   # address of list2
43223048
>>>
>>>
>>>
>>> list3 = list1 + list2   # concatenate list1 and list2 and create list3
>>> list3
[1, 2, 3, 11, 22, 33]
>

##Repetition Operator #
We can use * operator with lists too. It's syntax is:

sequence * n
The * operator replicates the list and then joins them. Here are some examples:

>>>
>>> list1 = [1, 5]
>>>
>>>
>>> list2 = list1 * 4  # replicate list1 4 times and assign the result to list2
>>>
>>> list2
[1, 5, 1, 5, 1, 5, 1, 5]
>>>
>>>

##List Methods #
The list class have many built-in methods which allows us to add element, remove element, update element and much more. The following table lists some common methods provided by the list class to manipulate lists.

Method	Description
appends(item)	adds an item to the end of the list.
insert(index, item)	inserts an item at the specified index. If index specified is greater than the last valid index, item is added to the end of the list.
index(item)	returns the index of the first occurrence of specified item. If the specified item doesn't exists in the list, an exception is raised.
remove(item)	removes the first occurrence of the specified item from the list. If the specified item doesn't exists in the list, an exception is raised.
count(item)	returns the number of times an item appears in the list.
clear()	removes all the element from the list.
sort()	sorts the list in ascending order.
reverse()	reverse the order of elements in the list.
extends(sequence)	appends the elements of the sequence to the end of the list.
pop([index])	removes the element at the specified index and returns that element. If index is not specified, it removes and returns last element from the list. When index is not valid, an exception is raised.
Note that all these method except count() modify the list object on which it is called.

The following shell session demonstrates how to use these methods:

append() method #
>>>
>>> list1 = [1,2,3,4,5,6]
>>>
>>> id(list1)
45741512        # address of list1
>>>
>>> list1.append(10)   # append 10 to list1
>>>
>>> list1               
[1, 2, 3, 4, 5, 6, 10]  
>>>
>>> id(list1)   # address remains unchanged
45741512
>>>

##sum
sum = 0
start = 100
end = 200
for i in range(start, end+1):
    sum += i    

print("Sum is", sum)


##Function to calculate the factorial of a number.
python101/Chapter-13/factorial.py

def factorial(n):
    f = 1
    for i in range(n, 0, -1):
        f *= n
        n -= 1

    print(f)

num = input("Enter a number: ")
factorial(int(num))

# a global variable
global_var = 200
def func():

    # local_var is a local variable
    # and is only available inside func() 
    local_var = 100

    print("Inside func() - local_var =", local_var)

    # accessing a global variable inside a function
    print("Inside func() - global_var =", global_var)


func()

print("Outside func() - global_var =", global_var)

# print("Outside func() - local_var =", local_var)  # ERROR: local_var is not available 


##python101/Chapter-13/multiple_arguments.py
def calc(num1, num2):
    print("Sum =", num1 + num2)
    print("Difference =", num1 - num2)
    print("Multiplication =", num1 * num2)
    print("Division =", num1 / num2)
    print()  # prints a blank line

calc(10, 20)

##Chapter-14/my_module.py

A_CONSTANT = 100

name = 'a variable'

def great_printer():
    print("first great_printer() definition")

def doo_hickey(arg):
    print("doo_hickey() called with argument:", arg)
Now we create a separate program (or client) named test_module.py in the same directory as my_module.py with the following code.

python101/Chapter-14/test_module.py

import my_module

my_module.doo_hickey('www')
my_module.great_printer()
print(my_module.A_CONSTANT)
print(my_module.name)

##using from
from my_module import doo_hickey, name

doo_hickey('x')
print(name)

##inheritance
import math

class Shape:

    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled


class Rectangle(Shape):

    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_breadth(self):
        return self.__breadth

    def set_breadth(self, breadth):
        self.__breadth = breadth

    def get_area(self):
        return self.__length * self.__breadth

    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius


r1 = Rectangle(10.5, 2.5)

print("Area of rectangle r1:", r1.get_area())
print("Perimeter of rectangle r1:", r1.get_perimeter())
print("Color of rectangle r1:", r1.get_color())
print("Is rectangle r1 filled ? ", r1.get_filled())
r1.set_filled(True)
print("Is rectangle r1 filled ? ", r1.get_filled())
r1.set_color("orange")
print("Color of rectangle r1:", r1.get_color())

c1 = Circle(12)

print("\nArea of circle c1:", format(c1.get_area(), "0.2f"))
print("Perimeter of circle c1:", format(c1.get_perimeter(), "0.2f"))
print("Color of circle c1:", c1.get_color())
print("Is circle c1 filled ? ", c1.get_filled())
c1.set_filled(True)
print("Is circle c1 filled ? ", c1.get_filled())
c1.set_color("blue")
print("Color of circle c1:", c1.get_color())

#multiple inheritance
class A:
    def explore(self):
        print("explore() method called")

class B:
    def search(self):
        print("search() method called")

class C:
    def discover(self):
        print("discover() method called")

class D(A, B, C):
    def test(self):
        print("test() method called")


d_obj = D()
d_obj.explore()
d_obj.search()
d_obj.discover()
d_obj.test()

##operator overloading
x, y = 2, 4

print("x = ", x, ", y =", y)

print("\nx + y =", x + y)
print("x.__add__(y) =", x.__add__(y))  # same as x + y

print("\nx * y = ", x * y)
print("x.__mul__(y) = ", x.__mul__(y))  # same as x * y

print("\nx / y = ", x / y)
print("x.__truediv__(y) = ", x.__truediv__(y))  # same as x / y

print("\nx ** y = ", x ** y)
print("x.__pow__(y) = ", x.__pow__(y))  # same as x ** y

print("\nx % y = ", x % y)
print("x.__mod__(y) = ", x.__mod__(y))  # same as x % y

print("\nx == y = ", x == y)
print("x.__eq__(y) = ", x.__eq__(y))  # same as x == y

print("\nx != y = ", x != y)
print("x.__ne__(y) = ", x.__ne__(y))  # same as x != y

print("\nx >= y = ", x >= y)
print("x.__ge__(y) = ", x.__ge__(y))  # same as x >= y

print("\nx <= y = ", x <= y)
print("x.__le__(y) = ", x.__le__(y))  # same as x <= y
print("------------------------------------------")

str1 = "special methods"

print("\nstr1 =", str1)

print("\n'ods' in str1 =", "ods" in str1)
print("str1.__contains__('ods') =", str1.__contains__("ods")) # same as "ods" in str1

print("\nlen(str1) =", len(str1))
print("str1.__len__() =", str1.__len__()) # same as len(str1)
print("------------------------------------------")

list1 = [11,33, 55]

print("\nlist1 =", list1)

print("\nlist1[1] =", list1[1])
print("list1.__getitem(1) =", list1.__getitem__(1)) # same as list1[1]
print("str(list1) =",str(list1)) 

##file commands:
read([num])	Reads the specified number of characters from the file and returns them as string. If num is omitted then it reads the entire file.
readline()	Reads a single line and returns it as a string.
readlines()	Reads the content of a file line by line and returns them as a list of strings.
write(str)	Writes the string argument to the file and returns the number of characters written to the file.
seek(offset, origin)	Moves the file pointer to the given offset from the origin.

#wrting a file
f = open("readme.md", "w")

f.write("First Line\n")
f.write("Second Line\n")
f.write("Third Line\n")

f.close()

##readline()
f = open("readme.md", "r")

# read first line
print("Ist line:", f.readline())  

# read the fist two characters in the second line
print("The first two characters in the 2nd line:", f.read(2), end="\n\n")

# read the remaining characters int the second line
print("Remaining characters in the 2nd line:", f.readline())

# read the next line
print("3rd line:", f.readline())  

# end of the file reached, so readline returns an empty string ""
print("After end of file :", f.readline())  

f.close()

##exception handling in python
try:
    num =  int(input("Enter a number: "))
    result = 10/num
    print("Result: ", result)    

except ZeroDivisionError:
    print("Exception Handler for ZeroDivisionError")
	
	try:
    num1 = int(input("Enter a num1: "))
    num2 = int(input("Enter a num2: "))

    result = num1 / num2
    print("Result: ", result)

except ZeroDivisionError:
    print("\nException Handler for ZeroDivisionError")
    print("We cant divide a number by 0")

except ValueError:
    print("\nException Handler for ValueError")
    print("Invalid input: Only integers are allowed")

except:
    print("\nSome unexpected error occurred")
    print("We cant divide a number by 0")

#finally()	
	import os
filename = input("Enter file name: ")

try:
    f = open(filename, "r")

    for line in f:
        print(line, end="")

    f.close()

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("You don't have the permission to read the file")

except FileExistsError:
    print("You don't have the permission to read the file")

except:
    print("Unexpected error while reading the file")

else:
    print("\nProgram ran without any problem")

finally:
    print("finally clause: This will always execute")
	
##factorial	
	
def factorial(n):
    if  not isinstance(n, int):
        raise RuntimeError("Argument must be int")

    if n < 0:
        raise RuntimeError("Argument must be >= 0")

    f = 1
    for i in range(n):
        f *= n
        n -= 1

    return f

try:
    print("Factorial of 4 is:", factorial(4))
    print("Factorial of 12 is:", factorial("12"))
except RuntimeError:
    print("Invalid Input")
	
##tuples
	tuple_a = ("alpha", "beta", "gamma")
print("tuple_a:", tuple_a)
print("Length of tuple_a:", len(tuple_a))  # len() function on tuple

tuple_b = tuple(range(1,20, 2)) # i.e tuple_b = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
print("\ntuple_b:", tuple_b)
print("Highest value in tuple_b:", max(tuple_b))   # max() function on tuple
print("Lowest value in tuple_b:",min(tuple_b))   # min() function on tuple
print("Sum of elements in tuple_b:",sum(tuple_b))   # sum() function on tuple

print("\nIndex operator ([]) and Slicing operator ([:]) : ")
print("tuple_a[1]:", tuple_a[1])
print("tuple_b[len(tuple_b)-1]:", tuple_b[len(tuple_b)-1])
print("tuple_a[1:]:", tuple_a[1:])

print("\nMembership operators with tuples: ")
print("'kappa' in tuple_a: ",'kappa' in tuple_a)
print("'kappa' not in tuple_b: ",'kappa' not in tuple_b)

print("\nIterating though elements using for loop")
print("tuple_a: ", end="")
for i in tuple_a:
    print(i, end=" ")

print("\ntuple_b: ", end="")
for i in tuple_b:
    print(i, end=" ")

##sets
print("\n\nComparing tuples: ")
print("tuple_a == tuple_b:", tuple_a == tuple_b)
print("tuple_a != tuple_b:", tuple_a != tuple_b)

print("\nMultiplication and addition operators on tuples: ")
print("tuple * 2:", tuple_a * 2)
print("tuple_b + (10000, 20000): ", tuple_b + (10000, 20000))

s1 = {4, 1, 9, 6}
>>> s1            # print the original set
{9, 1, 4, 6}
>>>
>>> id(s1)   # address of s1
35927880
>>>
>>> s1.add(0)   # add 0 to the set
>>> s1.add(10)  # add 10 to the set
>>>
>>> s1            # print the modified set
{0, 1, 4, 6, 9, 10}  
>>>
>>> id(s1)    # as sets are mutable objects, the address of s1 remains the same
35927880
>>>
>>> s1.remove(0)   # remove 0 from the set
>>> s1.remove(6)   # remove 6 from the set
>>>
>>> s1    # print s1 again
{1, 4, 9, 10}
>>>

##subset 
>>>
>>> A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> B = {1, 2, 3}
>>>
>>> A.issubset(B)   #  Is A subset of set B  ?
False
>>>
>>> B.issubset(A)   #  Is B subset of set A  ?
True
>>>
>>> B.issuperset(A)  #  Is B superset of set A  ?
False
>>>
>>> A.issuperset(B)  #  Is A subset of set B  ?
True
>>>

##dictionary
contacts = {
...     "tom": "122-444-333",
...     "jim": "412-1231-121",
...     "ron": "8912-121-1212",
...     "jake": "333-1881-121"
... }
>>>
>>> contacts   
{'jim': '412-1231-121', 'jake': '333-1881-121', 'tom': '122-444-333', 'ron': '89
12-121-1212'}
>>>

##calculator
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
  
##explicit conversion  
   num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))

##matrix multiplication
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
   
 ##quadratic equation  
   import cmath

a = 1
b = 5
c = 6

# To take coefficient input from the users
# a = float(input('Enter a: '))
# b = float(input('Enter b: '))
# c = float(input('Enter c: '))

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# Python program to display all the prime numbers within an interval

# change the values of lower and upper for a different result
lower = 900
upper = 1000

# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
		   
		   
## multiplication table		   
num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# use for loop to iterate 10 times


#fibonacciseries
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
for i in range(1, 11):
   print(num,'x',i,'=',num*i)
   
   lower = 100
upper = 2000

# To take input from the user
# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
	   
 # change this value for a different result
num = 16

# uncomment to take input from the user
#num = int(input("Enter a number: "))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate un till zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is",sum)
   
 
 # Change this value for a different result
terms = 10

# Uncomment to take number of terms from user
#terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

# display the result

print("The total terms is:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
   
   
 ##Python Program to find numbers divisible by thirteen from a list using anonymous function

# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,]

# use anonymous function to filter
result = list(filter(lambda x: (x % 3 == 0), my_list))

# display the result
print("Numbers divisible by 3 are",result)


# Python program to convert decimal number into binary, octal and hexadecimal number system

# Change this line for a different result
dec = 344

print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")

# Python program to find the H.C.F of two input number
# define a function
def computeHCF(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf

num1 = 54 
num2 = 24

# take input from the user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1,"and", num2,"is", computeHCF(num1, num2))


# Python Program to find the L.C.M. of two input number

# define a function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

# change the values of num1 and num2 for a different result
num1 = 54
num2 = 24

# uncomment the following lines to take input from the user
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))


# Python Program to find the factors of a number
# define a function
def print_factors(x):
   # This function takes a number and prints the factors

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

# change this value for a different result.
num = 320

# uncomment the following line to take input from the user
#num = int(input("Enter a number: "))
print_factors(num)


#hcf
def computeHCF(x, y):

   # This function implements the Euclidian algorithm to find H.C.F. of two numbers
   while(y):
       x, y = y, x % y

   return x

computeHCF(300, 400)

# Python program to display calendar of given month of the year
# import module
import calendar

yy = 2014
mm = 11

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


# Program to transpose a matrix using nested loop
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
   
   
   # Program to check if a string
#  is palindrome or not

# change this value for a different output
my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")
   
   
  # define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)


# Program to sort alphabetically the words form a string provided by the user

# change this value for a different result
my_str = "Hello this Is an Example With cased letters"

# uncomment to take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)
   
   
   # Program to perform different set operations like in mathematics

# define three sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};

# set union
print("Union of E and N is",E | N)

# set intersection
print("Intersection of E and N is",E & N)

# set difference
print("Difference of E and N is",E - N)

# set symmetric difference
print("Symmetric difference of E and N is",E ^ N)