import sys
#sys.stdin = open("input.txt","r")
n, limit = map(int, input().split())
p=list(map(int, input().split()))
p.sort()
count = 0
while len(p) >= 1:
    if len(p) == 1:
        count += 1
        break
    if p[-1] + p[0] > limit:
        count += 1
        p.pop(-1)
    else:
        count += 1
        p.pop(-1)
        p.pop(0)
print(count)