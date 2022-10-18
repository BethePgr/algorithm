import sys
sys.stdin = open("input.txt","r")
n,m = map(int, input().split())
list = [0] * (n+m+1)
kkk=[]
for i in range(1,n+1):
    for j in range(1,m+1):
        list[i+j] +=1
maxx = max(list)
for i in range(n+m+1):
    if list[i] == maxx:
        kkk.append(i)
print(kkk)

