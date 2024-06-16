x=int(input())
y=int(input())
while(y>0):
    if(y>x):
        x,y=y,x
    else:
        x,y=y,x-y
print(x)        