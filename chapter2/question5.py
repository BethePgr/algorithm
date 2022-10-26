"""
import sys
#sys.stdin = open("input.txt","r")
n,m = map(int, input().split())
a=list(map(int, input().split()))
count = 0
temp=0
for i in range(len(a)):
    temp=0
    for j in range(i,len(a)):
        temp += a[j]
        if temp == m:
            count +=1
            break
        if temp > m:
            break
print(count) #!!!!!!!!!!!!!!!!!!!시간복잡도 확인해보기!!!!!!!!!!!!!!!!!!!!!!!!
"""

import sys
#sys.stdin = open("input.txt","r")
n,m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt+= 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -=a[lt]
        lt+=1
print(cnt)

