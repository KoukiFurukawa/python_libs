from random import randint
from collections import defaultdict

check = defaultdict(int)
for i in range(1000):
    check[randint(1,6)] += 1

print(check)