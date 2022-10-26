"""
import sys
#sys.stdin = open("input.txt","r")
s = input()
letter = ""
for i in range(len(s)):
    if s[i].isdigit() == True:
        letter += str(s[i])
while letter[0] == "0":
    letter = letter[1:]
number = int(letter)
count = 0
for i in range(1,number+1):
    if number % i ==0:
        count+=1
print(number, count)
"""

import sys
#sys.stdin = open("input.txt","r")
s=input()
res = 0
for x in s:
    if x.isdecimal():
        res = res*10+int(x)
print(res)
cnt = 0
for i in range(1,res+1):
    if res % i == 0:
        cnt +=1
print(cnt)