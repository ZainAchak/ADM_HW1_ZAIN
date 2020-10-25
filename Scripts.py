### Insertion Sort###

#!/bin/python

import math
import os
import random
import re
import sys

def setArr(arr):
    arr = str(arr).replace("[", "")
    arr = str(arr).replace("]", "")
    arr = str(arr).replace(",", "")
    return arr

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    
    for i in range(1,n):
        toCheck = arr[i]
        j = i - 1
        while j>=0  and toCheck < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
            arr1 = setArr(arr)
            print(arr1)
    arr[j+1] = toCheck
    arr = setArr(arr)
    print arr

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    insertionSort1(n, arr)


### Viral Advertising ###

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    ppl = 5
    liked = 0
    days = n

    for i in range(1,days+1):
        liked += ppl//2
        ppl = ppl//2*3

    return liked
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


###  Number Line Jumps ###

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v1 - v2 == 0:
        return "NO"

    K1 = (x2-x1)%(v1-v2)
    K2 = (x2-x1)%(v2-v1)

    
    if x1 > x2 and v1 > v2:
        return "NO"
    elif x1 < x2 and v1 < v2:
        return "NO"
    if v1 == v2:
        return "NO"
    if K1 == 0 or K2 == 0:
        return "YES"
    else:
        return "NO"
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = raw_input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

### Birthday Cake Candles ###

#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    maxCandle = max(candles)
    candlestoBlow = candles.count(maxCandle)
    return candlestoBlow

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(raw_input().strip())

    candles = map(int, raw_input().rstrip().split())

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

###  Transpose and Flatten ###
import numpy
m = map(int,raw_input().split())
k = [map(int,raw_input().split()) for _ in xrange(m[0])]


n = numpy.array(k)
print numpy.transpose(n)
print n.flatten()

###  Shape and Reshape ###
import numpy as np


array = np.array(raw_input().split(' '),int)
print np.reshape(array,(3,3))

###  No Idea! ###
# Enter your code here. Read input from STDIN. Print output to STDOUT
n_m = raw_input().split()
n_m = map(int, n_m)
n = map(int, raw_input().split())
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))

counter = 0
for i in n:
    if i in A:
        counter += 1
    elif i in B:
        counter -= 1

print counter


###  Symmentric Difference  ### 

# Enter your code here. Read input from STDIN. Print output to STDOUT
int(raw_input())
N = raw_input().split()
Nint = set(list(map(int, N)))
int(raw_input())
M = raw_input().split()
Mint = set(list(map(int, M)))
res = []
for i in list(Nint.difference(Mint)):
    res.append(i)
for j in list(Mint.difference(Nint)):
    res.append(j)
for k in sorted(res):
    print k


###  Set.Union() Operation  ###

# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_n = int(raw_input())
eng_l = raw_input().split()
eng_s = set(map(int, eng_l))
fren_n = int(raw_input())
fren_l = raw_input().split()
fren_s = set(map(int, fren_l))

print len(eng_s.union(fren_s))


###  Set.Intersection Operation ###

# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_n = int(raw_input())
eng_s = raw_input().split()
eng_s = set(map(int, eng_s))
fren_n = int(raw_input())
fren_s = raw_input().split()
fren_s = set(map(int, fren_s))

print len(eng_s.intersection(fren_s))


###  set.symmetric_difference  ###
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(raw_input())
b = raw_input().split()
b = list(map(int, b))
c = int(raw_input())
d = raw_input().split()
d = list(map(int, d))

print len(set(b).symmetric_difference(set(d)))


###  Set Mutations  ###
a = int(raw_input())
A = set(map(int, raw_input().split()))
for i in range(int(raw_input())):
    s, b = raw_input().split()
    if s == 'intersection_update':
        A &= set(map(int, raw_input().split()))
    elif s == 'update':
        A |= set(map(int, raw_input().split()))
    elif s == 'symmetric_difference_update':
        A ^= set(map(int, raw_input().split()))
    else:
        A -= set(map(int, raw_input().split()))
print sum(A)  


### Set.add() ###

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
b = set()
for i in xrange(a):
    b.add(raw_input())

print len(b)


###  Set.discard() ###
n = input()
s = set(map(int, raw_input().split()))
a = input()

for i in xrange(a):
    k = []
    k = raw_input().split()
    if k[0] == 'pop':
        s.pop()
    elif k[0] == 'remove':
        s.remove(int(k[1]))
    elif k[0] == 'discard':
        s.discard(int(k[1]))
    else:
        print 'not a command'

print sum(s)


### Find a String ###
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)] == sub_string):
            count += 1
    return count


### Desinger Door Mat ###
# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int,raw_input().split())

for i in xrange(0,N/2): 
    print ('.|.'*i).rjust((M-2)/2,'-')+'.|.'+('.|.'*i).ljust((M-2)/2,'-')
print 'WELCOME'.center(M,'-')
for i in reversed(xrange(0,N/2)): 
    print ('.|.'*i).rjust((M-2)/2,'-')+'.|.'+('.|.'*i).ljust((M-2)/2,'-')


### Capatilize ###

# Complete the solve function below.
def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s

### String Formatiing
def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        l=len('{0:b}'.format(number))
        l=int(l)
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i,width=l))

### Alphabet Rangoli ###
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    
    pattern  = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        pattern.append((s[::-1]+s[1:]).center(4*size-3, "-"))
        
    print('\n'.join(pattern[:0:-1]+pattern))

###  The Minion Game ###
def minion_game(string):
    # your code goes here
    vowels_list = set(['a','e','i','o','u','A','E','I','O','U'])
    consonants = 0
    vowels = 0
 
    n = len(string)
    for i, l in enumerate(string):
        if l in vowels_list:
            vowels += n-i
        else:
            consonants += n-i
 
    if vowels == consonants:
        print "Draw"
    elif vowels > consonants:
        print "Kevin {}".format(vowels)
    else:
        print "Stuart {}".format(consonants)


### Merge the Tools ###
def merge_the_tools(string, k):
    # your code goes here
    chunks = len(string)/k

    for index in xrange(chunks):
        merge = ""
        T = string[index*k : (index+1)*k]
        for ch in T:
            if ch not in merge:
                merge += ch
        print merge

### MUtations ###
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character;
    string = ''.join(l);
    return string


### Whats Your Name ###
def print_full_name(a, b):
    print "Hello", a, b + "! You just delved into python."

### String Split and Join ###
def split_and_join(line):
    # write your code here
    line=line.split(" ")
    line='-'.join(line)
    return line

### Tuples ###
# Tuples in Python - Hacker Rank Solution
if __name__ == '__main__':
    n = int(raw_input())
    l = list()
    integers = raw_input().split()
    for i in integers:
            l.append(int(i))
    print hash(tuple(l))

### Lists ###
list = []
n = int(raw_input())
for i in range(n):
    a = raw_input().split()
    if len(a) == 3:
        eval("list." + a[0] + "(" + a[1] + "," + a[2] + ")")
    elif len(a) == 2:
        eval("list." + a[0] + "(" + a[1] + ")")
    elif a[0] == "print":
        print list
    else:
        eval("list." + a[0] + "()")

### Text Wrap ###

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

### Text Alignment ###
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Replace all ______ with rjust, ljust or center.

thickness = int(raw_input())  # This must me an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) +
          (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) / 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) +
          (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c +
          (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))


###  String Validators ###
if __name__ == '__main__':
    S = raw_input()
    print any([char.isalnum() for char in S])
    print any([char.isalpha() for char in S])
    print any([char.isdigit() for char in S])
    print any([char.islower() for char in S])
    print any([char.isupper() for char in S])


### Find the percentage ###
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    print("{0:.2f}".format(round(sum(student_marks[query_name]) / len(student_marks[query_name]), 2)))


### Nested Lists ###
if __name__ == '__main__':
    score_list = [];
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        score_list.append([name, score])
second_highest = sorted(set([score for name, score in score_list]))[1]
print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))


###  Find the Runner_up ###
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    m1 = max(arr)
    m2 = -9999999999
    for i in range(n):
        if arr[i] != m1 and arr[i] > m2:
            m2 = arr[i]
    print m2


### Print Function ###
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    x=""
    for i in range(1,n+1):
        x=x+str(i)
    print(x)


### Write a Function ###
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400 == 0:
        return True
    if year%100 == 0:
        return False
    if year%4 == 0:
        return True
    
    return False


### Python: Division ###
from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print (a//b)
    print (a/b)

### Arithmetic Operation ###
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a+b)
    print(a-b)
    print(a*b)


### Python If_Else ###
#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    if n%2 != 0:
        print ("Weird")
    else:
        if n >=2 and n<=5:
            print("Not Weird")
        elif n >= 6 and n <=20:
            print("Weird")
        elif n > 20:
            print("Not Weird")



### Say "Hello World" ###
if __name__ == '__main__':
    print "Hello, World!"













































