n=int(input())
arr=[0]*n
j=0
for i in range(n):
    packet=int(input())
    if packet!=0:
        arr[j]=packet
        j+=1
for i in range(n):
    print(arr[i],end=" ")        
        