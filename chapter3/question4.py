import sys
#sys.stdin = open("input.txt","r")
n,c = map(int, input().split())
list=[]
for i in range(n):
    temp = int(input())
    list.append(temp)
list.sort()
def Count(lenn):
    start = list[0]
    count = 1
    for i in range(1,len(list)):
        if list[i] -start >=lenn:
            count+=1
            start = list[i]
    return count


lt = list[0]
rt = list[-1]
count = 1
while lt <= rt:
    result = (rt+lt)//2
    if Count(result) >= c:
        answer = result
        lt = result + 1
    else:
        rt = result - 1
print(answer)
#!!!!!!!!!!!!!!!!!!!다시보기!!!!!!!!!!!!!!!!!!!!!!!!!!!!1