import sys
sys.stdin = open("input.txt","rt")
n=int(input())
result = 0
for i in range(n):
    temp = input().split()
    temp.sort()
    a,b,c = map(int,temp)
    if a == b and b == c:
        money = (10000+1000*a)
    elif a==b or b==c:
        money = (1000 + 100*b)
    elif a!=b and b!=c:
        money = (c*100)
    if money > result:
        result = money
print(result)