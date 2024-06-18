input1,input2,input3=list(map(int,input().split()))
count=set()
for i in range(input1//input2+1):
    for j in range(input1//input3+1):
        mcount=input1-input2*i-input3*j
        if mcount>0:
            count.add(mcount)
print(len(count))         
print(count)   
            