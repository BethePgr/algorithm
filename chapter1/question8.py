import sys
sys.stdin = open("input.txt","r")
n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    char=""
    for i in str(x):
        char = i + char
    return int(char)

def isprime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x % i ==0:
            return False
    return True
list = []
for i in range(n):
    k = reverse(str(a[i]))
    if isprime(k) == True:
        list.append(k)
print(list)