import sys
sys.stdin = open("input.txt","r")
a=list(range(21))
for i in range(10):
    s,e = map(int, input().split())
    for j in range((e-s)//2 +1):
        a[s+j],a[e-j] = a[e-j],a[s+j]
print(a[1:])
