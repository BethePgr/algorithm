import sys
sys.stdin = open("input.txt","r")
n=int(input())
a=list(map(int,input().split()))
min = 1000
avg=sum(a)/n
if int(avg + 0.5) == int(avg) + 1:
    avg = int(avg) + 1
else:
    avg = int(avg)
for i in range(len(a)):
    if min > abs(a[i] - avg):
        min = abs(a[i] - avg)
        temp = a[i]
        idx = i
    if min == abs(a[i] - avg):
        if temp <a[i]:
            temp=a[i]
            idx=i

print(avg,idx+1)