import sys
#sys.stdin = open("input.txt","r")
s=input()
stack=[]
answer=0
for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
    elif s[i] == ")":
        if s[i-1] == "(":
            stack.pop()
            answer+=len(stack)
        elif s[i-1] == ")":
            stack.pop()
            answer+=1
print(answer)