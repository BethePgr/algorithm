import sys
sys.stdin = open("input.txt","r")
n,m = map(int, input().split())
Music = list(map(int, input().split()))
lt = 1
rt = sum(Music)
answer= 0
def Count(mid):
    count = 1
    temp = mid
    for i in Music:
        if temp < i:
            count +=1
            temp = mid
        temp -= i
    return count

maxx = max(Music)

while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= maxx and Count(mid) <= m:
        answer = mid
        rt = mid-1
    else:
        lt = mid + 1
print(answer)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!다시보기!!!!!!!!!!!!!!!!!!!!!!1111