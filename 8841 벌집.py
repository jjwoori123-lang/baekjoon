n = int(input())
cnt = 1
n-=1
i = 1
while n:
    if n - (i * 6) >= 0:
        cnt+=1
        n -= i * 6
    else:
        break
    i+=1
if n:
    cnt+=1
print(cnt)