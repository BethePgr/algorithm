import sys
sys.stdin = open("input.txt","r")
s=input()
stack=[]
for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
