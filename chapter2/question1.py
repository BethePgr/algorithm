import sys
#sys.stdin = open("input.txt","r")
n = int(input())
# for i in range(n):
#     s=input()
#     s=s.upper()
#     letter=""
#     for i in s:
#         letter = i + letter
#     if s == letter:
#         print("YES")
#     else:
#         print("NO")

# for i in range(n):
#     s= input()
#     s=s.upper()
#     size = len(s)
#     for j in range(size//2):
#         if s[j] != s[-j-1]:
#             print("NO")
#             break
#     else:
#         print("YES")

for i in range(n):
    s=input()
    s=s.upper()
    if s == s[::-1]:
        print("#%d Yes" %(i+1))
    else:
        print("#"+(i+1) + " NO")