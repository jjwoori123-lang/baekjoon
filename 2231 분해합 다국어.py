import math
n =  int(input())
res = 0
for i in range(int(math.sqrt(n)), n):
    cnt = i
    key = i
    while i:
        cnt += (i % 10)
        i //=10
    if cnt == n:
        res = key
        break
print(res)