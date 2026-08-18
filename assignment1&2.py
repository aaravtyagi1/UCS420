
# 1 Hello World
# The code below prints the standard hello world statement.

print('Hello World')
# Assingment 1.1: WAP to print your name three times

# The code below prints a specific name three times in succession.

print('Aarav Tyagi')
print('Aarav Tyagi')
print('Aarav Tyagi')
# 2 Add numbers and Concatinate strings
# 2.1 Add two numbers
# The code below declares two numeric variables and adds them.

a=39
b=46

print(a+b)
print('a+b','=', a+b)
# 2.2 Concatinate two strings
# The code below concatenates a first name and a last name string.

first_name='Aarav'
last_name='Tyagi'
print('first_name','+','last_name','=',first_name+last_name)
# 2.3 Concatinate string with number
# The following code inserts a numeric string between two names.

first_name='Aarav'
last_name='Tyagi'
digit='89'
print('first_name','+','digit',''+',last_name','=',first_name+digit+last_name)
# Assingment 2.1: WAP to add three numbers and print the result.

# The script below calculates the sum of three predefined integer variables.

a=32
b=55
c=76
result=a+b+c
print('a','+','b','+','c','=',result)
# Assingment 2.2: WAP to concatinate three strings and print the result.

# The following block joins a title string with first and last name strings.

first_name='Aarav'
last_name='Tyagi'
title='Engineer'
print('Profession','+','first_name','+','last_name','=',title+first_name+last_name)
# 3 Input from user
# 3.1 Input two strings from user and concatinate them
# The program takes two names as input and prints them separated by a space.

first_name=input('Input the first name')
last_name=input('Input the last name')
print(first_name,' ',last_name)
# 3.2 Input two numbers from user and add them
a = int(input("Enter First No: "))
b = int(input("Enter Second No: "))
c = a + b
print (a, " + ", b, " --> ", c)
# 4 Loop
# 4.1 While Loop
# The loop below increments an index while printing a string up to 3 times.

i=0
while i<3:
  print('Aarav Tyagi')
  i=i+1
# 4.2 Range Function
# The examples show various ways to generate sequence lists using the range function.

print(range(0,-11,-1))
print(*range(1,11))
print("range(10) ------->", list(range(10)))
print("range(1,11) ------->", list(range(1,11)))
print("range(-10,-20) ------->", list(range(-10,-20,2)))
# 4.3 For loop
# 4.3.1 For loop - Version 1
# The code below prints numbers from 1 to 10 in a sequential loop.

for i in range(1,11):
 print(i)
# 4.4 Print table of 5
# This script formats a basic multiplication table for the number 5.

for i in range(1,11):
 print('5','✩',i,'=',5*i)
# 4.5 Sum all numbers from 1 to 10
# 4.5.1 Version 1
# This algorithm tracks cumulative addition incrementally from 1 through 10.

result=0
for i in range(1,11):
  for j in range(1,i):
    print(j,'+',end='')
  print(i, end='')
  result=result+i
  print('=',result)
# Assingment 4.1: WAP to print the table of 7, 9.

# These sequences compute the formatted multiplication tables for 7 and 9.

for i in range(1,11):
 print('7','✩',i,'=',7*i)

for i in range(1,11):
 print('9','✩',i,'=',9*i)
# Assingment 4.2: WAP to print the table of n and n is given by user.

# This block accepts user input to dynamically generate a multiplication table.

n=input('Enter the number')
for i in range(1,11):
 print(n,'✩',i,'=',int(n)*i)
# Assingment 4.3: WAP to add all the numbers from 1 to n and n is given by user.

# The code visually graphs the cumulative summation sequence up to a user-defined threshold.

n=int(input('Enter the number'))
result=0
for i in range(1,n+1):
  for j in range(1,i):
    print(j,'+',end='')
  print(i, end='')
  result=result+i
  print('=',result)
# 5 If-Else - Conditional Checking
# 5.1 Input two numbers from user and compare them
# The script requests two values from the user and applies conditional branching to identify the greater one.

#Input two numbers dfrom the user and compare them
froma= int(input("Enter the first number"))
b= int(input("Enter the second number"))
if(a>b):
    print("The first number is greater than the second number")
elif(b>a):
    print("The second number is greater than the first number")
else:
    print("Both entered numbers are equal")
    
# 5.2 Check weather a number is odd or even
# The modulo operator is used to verify the evenness of the input value.

#odd-even
a= int(input("Enter the number you want to verify"))
if(a%2==0):
    print("The entered number is even")
else:
    print("The entered number is odd")
# 5.3 Check weather a number is prime of not
# This logic iterates through possible divisors to determine if a number is prime.

#Check for prime
a= int(input("Enter the number you want to verify"))
flag=1
if(a<=1):
    print("The entered number is not valid")
    
for i in range(2,a):
    if(a%i==0):
        flag=0
        break
if(flag==0):
    print("The given number is not a prime")
else:
    print("The given number is PRIME")
        
# 5.4 Conditional Checking - Compare strings
a = input("Enter First String : ")
b = input("Enter Second String: ")
if a == b:
	print ("a == b")
elif a >= b:
	print ("a > b")
else:
	print ("a < b")
# Assingment 5.1: WAP to find max amoung three numbers and input from user. [Try max() function]

# This program utilizes the native max function to isolate the largest of three given numbers.

#Input three numbers from the ser and return the greatest number
a= int(input("Enter the first number"))
b= int(input("Enter the second number"))
c= int(input("Enter the third number"))
print("The greatest  among the numbers entered from the user is: ",max(a,b,c))
# Assingment 5.2: WAP to add all numbers divisible by 7 and 9 from 1 to n and n is given by the user.

# The code checks divisibility within a sequence and adds successful matches to an accumulator.

#WAP to add all numbers divisible by 7 and 9 from 1 to n as input by the user
n= int(input("Enter the number till which you want the sum"))
sum=0
for i in range(1,n+1):
    if(i%7==0):
        sum= sum+i
        continue
    if(i%9==0):
        sum= sum+i
        continue
print("The required sum is: ",sum)
# Assingment 5.3: WAP to add all prime numbers from 1 to n and n is given by the user.

# The block executes a nested iteration loop to compile the total sum of all identified primes within a range.

#WAP to add all prime numbers up to n as given by the user 
n= int(input("Enter the number till which you want the sum"))
sum=0
for i in range(2,n+1):
    flag=1
    for j in range(2,i):
        if(i%j==0):
            flag=0
            break
    if(flag==1):
        sum=sum+i
print("The required sum is: ",sum)
        
# 6 Functions
# 6.1 Add two numbers
# The Add function handles variables as arguments and returns their summation.

def Add(a,b):
    c=a+b
    return c

print("Add(10,9) --------->", Add(10,9))
print("Add(23,43) --------->", Add(23,43))
print("Add(36,59) --------->", Add(36,59))
print("Add(10,91) --------->", Add(10,91))
# 6.2 Prime number
# This boolean evaluation function identifies prime parameters using early return statements.

def checkPrime(a):
    for i in range(2,a):
        if(a%i==0):
            return False
        else:
            return True
a=int(input("Enter the number you want to check"))
if(checkPrime(a)):
    print("The number entered is Prime")
else:
    print("The number entered is Not Prime")
    
# 6.3 Add 1 to n
def AddN(n):
	s= sum(range(n+1))
	return s
print ("AddN(10)  --> ", AddN(10))
print ("AddN(20)  --> ", AddN(20))
print ("AddN(50)  --> ", AddN(50))
print ("AddN(200) --> ", AddN(200))
# Assingment 6.1: WAP using function that add all odd numbers from 1 to n, n is given by the user.

# The function loops until 'n' to aggregate all non-even numbers into a sum value.

def addOdd(n):
    sum=0
    for i in range(1,n+1):
        if(i%2!=0):
            sum=sum+i
    return sum
a=int(input("Enter the required number"))
print("The obtained sum is: ", addOdd(a))
# Assingment 6.2: WAP using function that add all prime numbers from 1 to n, n given by the user.

# This encapsulated function calculates the total value of primes within the argument boundary.

def addPrime(n):
    total = 0
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            total += i
    return total
a=int(input("Enter the required number: "))
print("The obtained sum is: ", addPrime(a))    
# 7 Math library
# Learning: Use math library

import math as m
print ("exp(-200)    --> ", m.exp(-100))  # Exponential function
print ("log(100,2)   --> ", m.log(100,2)) # Log
print ("log(100,10)  --> ", m.log(100,10))# Log
print ("log10(100)   --> ", m.log10(100)) # Log 10
print ("m.cos(30)    --> ", m.cos(29))    # cos
print ("m.sin(30)    --> ", m.sin(30))    # sin
print ("m.tan(30)    --> ", m.tan(32))    # tan
print ("m.sqrt(324)  --> ", m.sqrt(356))
print ("m.ceil(89.9) --> ", m.ceil(67.9))
print ("m.floor(89.9)--> ", m.floor(67.9))
# 8 Strings
# 8.1 Indexing in string
var = 'Elevator Music!'
print ("var      --> ", var)
print ("var[0]   --> ", var[0])
print ("var[1:5] --> ", var[1:5])
print ("var[:-5] --> ", var[:-5])
# 8.2 String length, upper, lower
var = 'Hello India!'
print ("String --> ", var)
print ("Length --> : ", len(var))
print ("Upper  --> : ", var.upper())
print ("Lower  --> : ", var.lower())
# 8.3 String formatting
name=input("Enter your name: ")
age=int(input("Enter your age : "))
price=float(input("Enter the book price: "))
s="\nYour name is %s, age is %d and book price is %f" %(name.upper(),age,price)
print (s)
# 8.4 String in Triple Quotes
paragraph_demo = """Hey this is Aarav tyagi and i am in batch 3p13 batch of computer science and engineering and technology ,
i am a third year student and have a keen learner too , i am a dsa enthsiast and a fullstack developer.
"""
print (paragraph_demo)
# 8.5 String strip
var =" Space   Association    "
print("String    --> ", var)
print("Length    --> ", len(var))
print("var strip --> ", var.strip())
print("Length of var after strip --> ", len(var.strip()))
# 8.6 String split
var =" Kennedy Space Cneter    "
print("String    --> ", var)
print("Length    --> ", len(var))
print("var split --> ", var.split())
print("var split --> ", var.split(' '))
print("var split --> ", var.split(','))
# Strip + Split
print("var split --> ", var.strip().split(','))
# 8.7 Count in string
var=" Space Force    "
print ("String       --> ", var)
print ("Count of ' ' --> ", var.count(' '))
print ("Count of 'a' --> ", var.count('a'))
print ("Count of 'n' --> ", var.count('an'))
# 8.8 Reverse a String
var="Elon Musk"
print ("String    --> ", var)
print ("var[::1]  --> ", var[::1])
print ("var[::2]  --> ", var[::2])
print ("var[::-1] --> ", var[::-1])
print ("var[::-2] --> ", var[::-2])

var=var[::-1]
print ("var after reverse --> ", var)
# 8.9 Palindrome
s1="nitin"
s2="edible"
s3="madam"
s4="crow"
print ("s1 --> ", s1==s1[::-1])
print ("s2 --> ", s2==s2[::-1])
print ("s3 --> ", s3==s3[::-1])
print ("s4 --> ", s4==s4[::-1])


##-----------ASSIGNMENT 2-----------------#


# 1. List Operations
# 1. Take your roll number. Extract its individual digits, and multiply each digit by 10
roll_number = "1024160067" 
L = [int(digit) * 10 for digit in roll_number]

# Print L
print(" Original List L:", L)

# Add two numbers (append and insert)
L.append(89)
print(" After append(89)  -->", L) 
L.insert(2, 45)
print(" After insert(2, 45)  -->", L)

# Remove two elements 
L.remove(40)
print(" After remove(40)  -->", L) 
popped_val = L.pop()
print(f" After pop() which removed {popped_val}  -->", L) 

# Sort L
L.sort()
print("Sorted ascending  -->", L)
L.sort(reverse=True)
print("Sorted descending  -->", L)

# Slicing
print(" First three elements  -->", L[:3])
print(" Last three elements  -->", L[-3:])

#  List comprehension based on average
avg = sum(L) / len(L)
L_filtered = [x for x in L if x > avg]
print(f" Elements greater than average ({avg}):", L_filtered)
#  Original List L: [10, 0, 20, 40, 10, 60, 0, 0, 70, 90]
#  After append(99)  --> [10, 0, 20, 40, 10, 60, 0, 0, 70, 90, 99]
#  After insert(2, 55)  --> [10, 0, 55, 20, 40, 10, 60, 0, 0, 70, 90, 99]
#  After remove(40)  --> [10, 0, 55, 20, 10, 60, 0, 0, 70, 90, 99]
#  After pop() which removed 99  --> [10, 0, 55, 20, 10, 60, 0, 0, 70, 90]
# Sorted ascending  --> [0, 0, 0, 10, 10, 20, 55, 60, 70, 90]
# Sorted descending  --> [90, 70, 60, 55, 20, 10, 10, 0, 0, 0]
#  First three elements  --> [90, 70, 60]
#  Last three elements  --> [0, 0, 0]
#  Elements greater than average (31.5): [90, 70, 60, 55]

# 2. Tuple Operations
# 2. Create a tuple containing 8 marks (first 8 values from Q1 list)
scores = tuple(L[:8])
print("Scores Tuple:", scores)

# Highest and lowest scores
high = max(scores)
low = min(scores)
print(f" Highest score: {high} at index {scores.index(high)}")
print(f" Lowest score: {low}, occurs {scores.count(low)} times")

# Reverse the tuple
reversed_scores = list(scores)[::-1]
reversed_scores2 = list(scores)
reversed_scores2.sort(reverse=True)
print(reversed_scores2)
print("Reversed tuple as list:", reversed_scores)
# tuples cannot be reversed in place because they are immutable and their internal state cannot be modified.

# User input search
try:
    search_val = int(input("iii. Enter a score to search: "))
    if search_val in scores:
        print(f"Index of {search_val}:", scores.index(search_val))
    else:
        print("Not present")
except ValueError:
    print("Invalid input.")

# Change element directly
try:
    scores[0] = 100
except TypeError as e:
    print("iv. Error caught:", e)
# TypeError happens because tuples are immutable and do not support item assignment. This is not the case with lists, as they are mutable.

# Unpack the tuple
first, second, *remaining = scores
print("v. First:", first, "| Second:", second, "| Remaining:", remaining)
# Scores Tuple: (90, 70, 60, 55, 20, 10, 10, 0)
#  Highest score: 90 at index 0
#  Lowest score: 0, occurs 1 times
# [90, 70, 60, 55, 20, 10, 10, 0]
# Reversed tuple as list: [0, 10, 10, 20, 55, 60, 70, 90]
# Index of 55: 3
# iv. Error caught: 'tuple' object does not support item assignment
# v. First: 90 | Second: 70 | Remaining: [60, 55, 20, 10, 10, 0]
# 3. Random Numbers and Comprehensions
# This section seeds a random number generator and uses list comprehensions to isolate odds, evens, and primes from a generated dataset[cite: 5].

import random

# 3. Set random seed
random.seed(1024160067) 

# Generate 100 random numbers
rand_nums = [random.randint(100, 900) for _ in range(100)]
print(" First 10 random numbers:", rand_nums[:10])

# Count and print odd numbers
odds = [x for x in rand_nums if x % 2 != 0]
print(f" Odd numbers count: {len(odds)}\nList: {odds}")

# Count and print even numbers
evens = [x for x in rand_nums if x % 2 == 0]
print(f" Even numbers count: {len(evens)}\nList: {evens}")

# Prime numbers
def check_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

primes = [x for x in rand_nums if check_prime(x)]
print(f" Prime numbers count: {len(primes)}\nList: {primes}")

# Most frequent number
most_frequent = max(set(rand_nums), key=rand_nums.count)
print(f" Most frequent number: {most_frequent}, Occurrences: {rand_nums.count(most_frequent)}")
#  First 10 random numbers: [884, 460, 376, 481, 899, 675, 396, 365, 704, 759]
#  Odd numbers count: 49
# List: [481, 899, 675, 365, 759, 703, 207, 683, 237, 635, 731, 419, 791, 327, 103, 805, 387, 403, 193, 677, 451, 883, 871, 691, 875, 503, 491, 509, 577, 145, 795, 575, 183, 891, 363, 689, 767, 361, 489, 367, 539, 591, 709, 381, 461, 429, 331, 187, 645]
#  Even numbers count: 51
# List: [884, 460, 376, 396, 704, 876, 210, 792, 396, 306, 636, 128, 152, 588, 314, 530, 716, 210, 594, 848, 562, 538, 538, 726, 886, 264, 794, 804, 522, 698, 502, 198, 404, 254, 324, 890, 732, 762, 692, 718, 472, 798, 268, 866, 498, 530, 842, 242, 220, 612, 192]
#  Prime numbers count: 15
# List: [683, 419, 103, 193, 677, 883, 691, 503, 491, 509, 577, 367, 709, 461, 331]
#  Most frequent number: 530, Occurrences: 2
# 4. Set Operations
# This section builds sets from the initial digits and performs set mathematics including unions, intersections, and differences[cite: 5].

# 4. Sets from first 8 digits of roll number
roll_digits = [int(d) for d in "1024160066"][:8]
A = {d * 7 for d in roll_digits}
B = {d * 9 for d in roll_digits}
print("Set A:", A)
print("Set B:", B)

#  Union
print("    Union of A and B:", A.union(B))

#  Intersection
print("    Intersection of A and B:", A.intersection(B))

#  Difference
print("   A - B:", A.difference(B))
print("   B - A:", B.difference(A))
# difference() finds elements unique to one specific set, while symmetric_difference() finds elements unique to both sets combined.

#  Symmetric difference
print(" Symmetric difference of A and B:", A.symmetric_difference(B))

# Subset and Superset
print(" Is A a subset of B?", A.issubset(B))
print(" Is B a superset of A?", B.issuperset(A))

#  Discard user input
try:
    valRemove = int(input("xi. Enter a value to remove from A: "))
    A.discard(valRemove)
    print("Set A after discard attempt:", A)
except ValueError:
    print("Invalid input.")
# discard() is safer than remove() because it quietly does nothing if the element is missing. The remove() throws a Key error
# Set A: {0, 7, 42, 14, 28}
# Set B: {0, 36, 9, 18, 54}
#     Union of A and B: {0, 36, 7, 9, 42, 14, 18, 54, 28}
#     Intersection of A and B: {0}
#    A - B: {42, 28, 14, 7}
#    B - A: {9, 18, 36, 54}
#  Symmetric difference of A and B: {7, 9, 14, 18, 28, 36, 42, 54}
#  Is A a subset of B? False
#  Is B a superset of A? False
# Set A after discard attempt: {0, 42, 14, 28}
# 5. Dictionary Operations
# This section outlines dictionary key-value manipulation, merging datasets, and safe iteration fallbacks[cite: 5].

# 5. Dictionary operations
my_dict = {
    "name": "Aarav Tyagi",
    "roll_no": "1024160067",
    "branch": "Computer Science",
    "age": 20,
    "city": "Ambala"
}

#  Rename key
my_dict["location"] = my_dict.pop("city")
print("i. Dictionary after renaming city to location:", my_dict)

# Add CGPA
my_dict["cgpa"] = 10.0
print("ii. Dictionary after adding CGPA:", my_dict)

# Increase age
my_dict["age"] += 1
print("iii. Dictionary after updating age:", my_dict)

#  Delete branch using pop() and del
dict_copy1 = my_dict.copy()
dict_copy2 = my_dict.copy()
popped_val = dict_copy1.pop("branch")
del dict_copy2["branch"]
# pop() removes the key and returns its value so it can be used, while del purely deletes the mapping without returning anything.

#  Iterate items
print("  Key-Value pairs:")
for key, value in my_dict.items():
    print(f"{key} -> {value}")

#  Safe key check
if "email" in my_dict:
    print("   Email:", my_dict["email"])
else:
    print("   Email not found in dictionary. Reconfigure and add the required field.")

# Merge dictionaries
friend_dict = {
    "name": "Elon Musk",
    "roll_no": "1024160420",
    "branch": "Space Technology",
    "age": 21,
    "location": "South Africa"
}
merged_dict = {**my_dict, **friend_dict}
print("   Merged Dictionary:", merged_dict)
# When dictionaries share a key, the value from the rightmost dictionary (dict2) is prioritised and overwrites the earlier value.

# Dictionary comprehension for strings
str_dict = {k: v for k, v in my_dict.items() if isinstance(v, str)}
print("    String-only dictionary:", str_dict)
# i. Dictionary after renaming city to location: {'name': 'Aarav Tyagi', 'roll_no': '1024160067', 'branch': 'Computer Science', 'age': 20, 'location': 'Ambala'}
# ii. Dictionary after adding CGPA: {'name': 'Aarav Tyagi', 'roll_no': '1024160067', 'branch': 'Computer Science', 'age': 20, 'location': 'Ambala', 'cgpa': 10.0}
# iii. Dictionary after updating age: {'name': 'Aarav Tyagi', 'roll_no': '1024160067', 'branch': 'Computer Science', 'age': 21, 'location': 'Ambala', 'cgpa': 10.0}
#   Key-Value pairs:
# name -> Aarav Tyagi
# roll_no -> 1024160067
# branch -> Computer Science
# age -> 21
# location -> Ambala
# cgpa -> 10.0
#    Email not found in dictionary. Please register yourself first.
#    Merged Dictionary: {'name': 'Elon Musk', 'roll_no': '1024160420', 'branch': 'Space Technology', 'age': 21, 'location': 'South Africa', 'cgpa': 10.0}
#     String-only dictionary: {'name': 'Aarav Tyagi', 'roll_no': '1024160067', 'branch': 'Computer Science', 'location': 'Ambala'}
 
