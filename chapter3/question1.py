import sys
#sys.stdin = open("input.txt","r")
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
l = 0
r = n-1
while l <= r:
    mid = (l+r)//2
    if a[mid] == m:
        break
    elif a[mid] > m:
        r = mid - 1
    elif a[mid] < m:
        l = mid + 1
print(mid+1)