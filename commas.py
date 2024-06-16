n=int(input())
curr=1000
comma=1
res=0
while curr<=n:
   next=curr*1000
   number=min(n-curr+1,next-curr)
   res=res+number*comma
   curr=next
   comma=comma+1
print(res)   