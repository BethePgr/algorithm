import sys
#sys.stdin = open("input.txt","r")
n = int(input())
list=[]
for i in range(n):
    a,b = map(int, input().split())
    list.append([a,b])
list.sort(reverse=True)
largest = 0
count = 0
for i in list:
    if i[1] > largest:
        largest = i[1]
    else:
        count += 1
count = n - count
print(count)