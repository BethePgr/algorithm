import sys
sys.stdin = open("input.txt","r")
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
print(count) #시간복잡도 확인해보기

