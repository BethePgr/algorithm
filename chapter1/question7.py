import math
# import sys
# sys.stdin = open("input.txt","r")
# n=int(input())
# list = [0] * (n+1)
# count = 0
# for i in range(2,n+1):
#     if list[i] == 0:
#         count+=1
#         for j in range(i,n+1,i):
#             list[j] = 1
# print(count)

# def solution(number):
#     list = [0] * (number + 1)
#     answer=[]
#     for i in range(2,number+1):
#         if list[i] == 0:
#             answer.append(i)
#             for j in range(i,number+1,i):
#                 list[j] = 1
#     return len(answer)
#
# print(solution(100000))

def solution(number):
    n = int(number ** (1/2))+1
    list = [0] * (number + 1)
    for i in range(2,n):
        if list[i] == 0:
            for j in range(i+i,number+1,i):
                list[j] = 1
    count = 0
    for i in range(2,len(list)):
        if list[i] == 0:
            count+=1
    return count
print(solution(16))