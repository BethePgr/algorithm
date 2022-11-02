import sys
#sys.stdin = open("input.txt","r")
n = int(input())
a=list(map(int, input().split()))
lt = 0
rt = n-1
list=[0]
answer=""
while True:
    if len(a) == 1 and a[0] > list[-1]:
        list.append(a.pop(0))
        answer+="L"
    elif len(a) == 1 and a[0] < list[-1]:
        break

    if a[-1] > a[0]:
        if a[0] > list[-1]:
            list.append(a.pop(0))
            answer+="L"
        elif a[0] < list[-1] and a[-1] > list[-1]:
            list.append(a.pop(-1))
            answer+="R"
        elif a[0] < list[-1] and a[-1] < list[-1]:
            break
    elif a[-1] < a[0]:
        if a[-1] > list[-1]:
            list.append(a.pop(-1))
            answer+="R"
        elif a[-1] < list[-1] and a[0] > list[-1]:
            list.append(a.pop(0))
            answer+="L"
        elif a[-1] < list[-1] and a[0] < list[-1]:
            break
print(len(answer))
print(answer)