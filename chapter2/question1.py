import sys
sys.stdin = open("input.txt","r")
n = int(input())
for i in range(n):
    s=input()
    s=s.upper()
    letter=""
    for i in s:
        letter = i + letter
    if s == letter:
        print("YES")
    else:
        print("NO")

