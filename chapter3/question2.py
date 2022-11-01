import sys
#sys.stdin = open("input.txt","r")
k, n = map(int, input().split())
answer=0
list= []
def Count(x):
    count = 0
    for i in list:
        count += i//x
    return count
for i in range(k):
    temp = int(input())
    list.append(temp)
largest = max(list)
lt = 1
rt = largest
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid)>=n:
        answer = mid
        lt = mid+1
    elif Count(mid) < n:
        rt = mid - 1
print(answer)