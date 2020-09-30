import math
number = int(input())
base = int(input())

if base <= 1:
    print(round(math.log(number), 2))
else:
    print(round(math.log(number, base), 2))
