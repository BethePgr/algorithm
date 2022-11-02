import sys
#sys.stdin = open("input.txt","r")
n = int(input())
list = []
for i in range(n):
    s,e = map(int, input().split())
    list.append([s,e])
list.sort(key = lambda x : (x[1],x[0]))
count = 0
temp = 0
for i in list:
    if i[0] >=temp:
        count += 1
        temp = i[1]
print(count)