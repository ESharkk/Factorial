import math
lst = []

n = int(input())

if 1 <= n <= 100:
    for i in range(0, n):
        ele = int(input())
        if 1 <= ele <= 100:
            lst.append(ele)
else:
    raise ValueError("n must be between 1 and 100 inclusive.")

factorials = [math.factorial(ele) for ele in lst]

for fact in factorials:
    print(fact)