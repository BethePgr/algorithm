import sys
#sys.stdin = open("input.txt","r")
n = int(input())
a=list(map(int, input().split()))
list = [0] * n
for i in range(len(a)):
    number = 0
    for j in range(len(a)):
        if list[j] == 0:
            number += 1
        if number > a[i]:
            list[j] = i + 1
            break
for i in list:
    print(i, end = " ")
[0 0 0 0 0 0 0 0]
"5 3 4 0 2 1 1 0"