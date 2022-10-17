'''
def add(a, b):
	return a * b

'''
'''	
import math
from math import factorial
print(factorial(6))
print(dir(math))

'''

'''
#from math import *
#from math import sqrt

from math import sqrt , factorial
print(factorial(5))
print(int(sqrt(16)))

'''
'''

from datetime import date
today = date.today()

print(today)

from datetime import datetime
today = datetime.now()


print(today)

'''

'''

import math
print(math.sqrt(225.46))
print(dir(math))
print(math.degrees(30))
print(math.sin(30))
print(math.cos(80))

'''

'''

from datetime import datetime
today = datetime.now()
print(today)

'''

'''

from functools import reduce
l = [1, 2, 3, 4, 5]     
def i(c, d):
    return c + d
x = reduce(i ,l)
print(x)


'''

'''

from itertools import combinations, permutations
l = [1, 2, 3]	
print([list(permutations(l, x)) for x in range(1, len(l) + 1)])

'''


'''

from itertools import combinations

x = [1, 2, 3]
def combs(x):
	return [c for i in range(len(x)+1) for c in combinations(x, i)]
print(i)

'''

'''
import math
print(math.sqrt(225.46))

'''
'''
l = [1, 4, 5, 2, 3]
print(sum(l) // len(l))
print(max(l))
print(min(l))

from itertools import combinations
a = [1, 2, 3]
x = combinations(a, 1)
for i in list(a):
	print(i)
'''
'''
math = 19
print(dir(math))

'''

'''

x=[6,1,3,4]
for i in x:
	if i/2==0:
		continue
		print('i is a even number')
	else:
		print(i)
'''
'''

l =[2,4,7,8]
for i in l:
	if(i % 2 == 0):
		print(i)

	else:
		print(i, "number")
		break
		print('outside the for loop')

'''