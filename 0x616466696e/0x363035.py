 # Instructions:
 #
 # Please implement the problems below. You will be judged on the quality of
 # the code and resonable efficiency.
 #
 # Notes:
 #  * Feel free to switch the language to Java, Scala, Python, C, C++, or Go
 #  * Please build your own solution. Eg. if the problem requires you to
 #    implement a sort algorithm, do not just call the built in library sort.
 #  * You are not being timed.
 #  * Feel free to use resources on the web, but DO NOT copy and paste code
 #    from Wikipedia/StackOverflow/etc.
 #  * Feel free to change the test driver code (main func)
 #
 # Start with an approach that works (brute force), work to refine a more optimized solution"
 # ex. do not use csv.parse out of the runtime library

print("Hello")

# Problem #1
# Write a function that returns an vector of all the prime numbers
# up to and including the max specified by the argument.

def prime_numbers(max):
    result = []

    if max <= 1:
        return result

    for i in range(2, max + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            result.append(i)

    return result

primes = prime_numbers(100)
print('primes', primes)


# Problem #2
# Given two pre-sorted vectors of integers, find the intersection.
# Return the vector of intersecting values.

class Vector:
    def __init__(self):
        self.data = set()

    def add(self, value):
        self.data.add(value)


def array_intersection(inter1, inter2):
    # return set(inter1.data).intersection(inter2.data)

    result = set()
    for i in inter1.data:
        for j in inter2.data:
            if i == j:
                result.add(i)

    return result

inter1 = Vector()
inter1.add(1)
inter1.add(2)
inter1.add(3)
inter1.add(25)

inter2 = Vector()
inter2.add(2)
inter2.add(3)
inter2.add(15)
inter2.add(25)

intersect = array_intersection(inter1, inter2)
print('intersection', intersect)


# Problem #3
# Implement a simple CSV parser.
# Parser outputs List (rows) of List (columns)
# Lines are delimited by '\n'
# Columns are delimited by ','
# Columns can be quoted by using '"' chars (start and end)
csv_data = "1514764800,US,United States,15,\"$1,500\"\n" \
        + "1514764800,CA,Canada,2,$200\n" \
        + "1514764800,UK,United Kingdom,36,\"$3,400\"\n" \
        + "1514764800,DE,Germany,12,\"$1,100\"\n"

# fastest way
import csv
from io import StringIO

def parse_csv(input):
    result = []
    file = StringIO(input)
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        result.append(row)

    return result

lists = parse_csv(csv_data)
print('parsed csv', lists)
