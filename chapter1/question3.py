import sys
sys.stdin=open("input.txt","rt")
n,k=map(int,input().split())
a=list(map(int,input().split()))
answer_list=set()
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            answer_list.add(a[i] + a[j] + a[m])
answer_list = list(answer_list)
answer_list.sort(reverse=True)
print(answer_list[k-1])