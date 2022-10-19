import sys
sys.stdin = open("input.txt","r")
n= int(input())
a = list(map(int, input().split()))
count = 0
sum = 0
for i in range(len(a)):
    if a[i] == 1:
        count +=1
        sum+=count
    else:
        count = 0
print(sum)

#end