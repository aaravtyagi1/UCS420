
print("Hello World")
print("Aarav Tyagi")
print("Aarav Tyagi")
print("Aarav Tyagi")
i = 5
j = 10 
print(i+j)

x =  'abc'
y = 'def'
w='ghi'
z=  x+y
print(z)

x1 =  'abc'
y1 = 3
z1=  x1+ str(y1)
print(z1)

k = 15
l = i+j+k
print(l)

o = x+y+w
print(o)

p  = int(input("enter p : "))
print(p)


for k in range(1, 11) :
    print(k*10)

# this prints 1 to 10 using range 

print(list(range(10, 100, 10)))# first one is starting value second is the largest value and third is step value
print(list(range(-10, -20, -2)))

# ASSIGNMENT 2
import random
import math
from collections import Counter

roll_number = 12345678
digits = [int(d) for d in str(roll_number)]

L = [digit * 10 for digit in digits]

print("Q1 i:", L)

L.append(25)
print("Q1 ii append:", L)

L.insert(2, 35)
print("Q1 ii insert:", L)

L.remove(25)
print("Q1 iii remove:", L)

L.pop(2)
print("Q1 iii pop:", L)

L.sort()
print("Q1 iv ascending:", L)

L.sort(reverse=True)
print("Q1 iv descending:", L)

print("Q1 v first three:", L[:3])
print("Q1 v last three:", L[-3:])

average = sum(L) / len(L)
greater_than_average = [x for x in L if x > average]
print("Q1 vi:", greater_than_average)


scores = tuple(L[:8])

highest_score = max(scores)
highest_index = scores.index(highest_score)

lowest_score = min(scores)
lowest_count = scores.count(lowest_score)

print("Q2 i highest score:", highest_score)
print("Q2 i highest score index:", highest_index)
print("Q2 i lowest score:", lowest_score)
print("Q2 i lowest score count:", lowest_count)

reversed_scores = list(reversed(scores))
print("Q2 ii:", reversed_scores)

user_score = int(input("Enter a score: "))

if user_score in scores:
    print("Q2 iii index:", scores.index(user_score))
else:
    print("Q2 iii: Score not present")

try:
    scores[0] = 100
except TypeError as e:
    print("Q2 iv error:", e)

first_score, second_score, *remaining_scores = scores
print("Q2 v:", first_score, second_score, remaining_scores)


random.seed(roll_number)

random_numbers = [random.randint(100, 900) for _ in range(100)]

odd_numbers = [x for x in random_numbers if x % 2 != 0]
even_numbers = [x for x in random_numbers if x % 2 == 0]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [x for x in random_numbers if is_prime(x)]

print("Q3 ii odd count:", len(odd_numbers))
print("Q3 ii odd numbers:", odd_numbers)

print("Q3 iii even count:", len(even_numbers))
print("Q3 iii even numbers:", even_numbers)

print("Q3 iv prime count:", len(prime_numbers))
print("Q3 iv prime numbers:", prime_numbers)

frequency = Counter(random_numbers)
most_frequent_number, frequency_count = frequency.most_common(1)[0]

print("Q3 v most frequent number:", most_frequent_number)
print("Q3 v frequency:", frequency_count)


A = {digit * 7 for digit in digits}
B = {digit * 9 for digit in digits}

print("Q4 sets")
print("A:", A)
print("B:", B)

union_set = A.union(B)
print("Q4 vi union:", union_set)

intersection_set = A.intersection(B)
print("Q4 vii intersection:", intersection_set)

A_minus_B = A.difference(B)
B_minus_A = B.difference(A)

print("Q4 viii A - B:", A_minus_B)
print("Q4 viii B - A:", B_minus_A)

symmetric_difference = A.symmetric_difference(B)
print("Q4 ix symmetric difference:", symmetric_difference)

print("Q4 x A subset of B:", A.issubset(B))
print("Q4 x B superset of A:", B.issuperset(A))

X = int(input("Enter a value X: "))
A.discard(X)
print("Q4 xi A after discard:", A)


my_dict = {
    "name": "Your Name",
    "roll_no": str(roll_number),
    "branch": "Your Branch",
    "age": 20,
    "city": "Your Home City"
}

my_dict["location"] = my_dict.pop("city")
my_dict["cgpa"] = 8.5

my_dict["age"] += 1

dict_pop = my_dict.copy()
dict_pop.pop("branch")

dict_del = my_dict.copy()
del dict_del["branch"]

print("Q5 iv pop:", dict_pop)
print("Q5 iv del:", dict_del)

for key, value in my_dict.items():
    print(f"{key} → {value}")

if "email" in my_dict:
    print("Email:", my_dict["email"])
else:
    print("Email key does not exist")

friend_dict = {
    "name": "Rahul",
    "roll_no": "87654321",
    "branch": "CSE",
    "age": 21,
    "city": "Delhi"
}

merged_dict = {**my_dict, **friend_dict}
print("Q5 vii merged dictionary:", merged_dict)

string_values = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("Q5 viii string values:", string_values)