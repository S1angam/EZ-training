n=int(input("enter the size of array->"))
arr=list(map(int,input().split()))
pro=0
dlist=[]
k=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]+arr[j]==18:
            if arr[i]>arr[j]:
                k=arr[i]*arr[j]
            if k>pro:
               pro=k
               dlist.append(arr[i])
               dlist.append(arr[j])
print(dlist)               
                
                
            
