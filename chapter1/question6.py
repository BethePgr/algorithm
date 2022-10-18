import sys
sys.stdin = open("input.txt","r")
n = int(input())
a=list(map(int, input().split()))
def digit_sum(x):
    sum = 0
    while True:
        sum += x % 10
        x = x//10
        if x == 0:
            break
    return sum
number = 0
for i in a:
    if digit_sum(i) > number:
        number = digit_sum(i)
        temp=i
print(temp)