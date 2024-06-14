a=list(map(int,input().split()))
max=0
max1=0
for i in a:
      if i>max:
          max=i
for j in a:
    if j>max1 and j<max:
        max1=j
avg=(max+max1)/2
ans=0
for i in a:
    if i>avg:
        ans+=i
print(ans)        
        