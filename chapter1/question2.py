import sys
sys.stdin=open("input.txt","rt")
T=int(input())
for t in range(T):
    n,start,end,k = map(int,input().split())
    answer_list = list(map(int,input().split()))
    answer_list=answer_list[start-1:end]
    answer_list.sort()
    print(answer_list[k-1])