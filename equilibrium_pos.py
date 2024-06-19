a=int(input())
arr=list(map(int,input().split()))
flag=True
for i in range(len(arr)):
    if sum(arr[:i+1])==sum(arr[i+1:]):
        flag=False
        print(i+1)
        break
if flag:
    print("NOT FOUND")    