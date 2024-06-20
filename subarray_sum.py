def solve(nums,n):
    currsum=nums[0]
    maxsum=nums[0]
    for num in nums[1:]:
        maxsum=max(num,maxsum+num)
        currsum=max(currsum,maxsum)
    return currsum
n=int(input())
arr=list(map(int,input().split())) 
print(solve(arr,n))   