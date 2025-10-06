import random
import numpy
num=[]
for i in range(15):
    num.append(random.randint(1,100))
print(num)
print(sum(num))
print(max(num))
print(min(num))
prom=sum(num)/len(num)
print(prom)
num2=num[::-1]
print(num[::-1])
print(num[-1])
print(set(num))
numor=sorted(num)
print(f"numeros ordenados{numor}")
