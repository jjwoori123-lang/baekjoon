n  = int(input())
arr = list(map(int, input().split()))
a,b = map(int, input().split())
cnt = 0
for ar in arr:
    if ar <= a and ar: cnt +=1
    else:
        if ar % a ==0: cnt += (ar // a)
        else: cnt += ((ar // a) + 1)
print(cnt)
print(n// b, n % b)