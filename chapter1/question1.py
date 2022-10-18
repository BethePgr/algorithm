def solution(n,k):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count+=1
        if count == k:
            return i
    if k > count:
        return -1
print(solution(8,4))
print(solution(25,5))
print(solution(100,5))
print(solution(100,7))
print(solution(1000,12))