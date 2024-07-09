nums = list(map(int,input().split()))
jump = int(input())+1
left = int(input())
i = jump
print(nums,jump,left)
while len(nums) > left:
    del nums[i]
    i-=1
    i+=jump
    print(i)
    while i >= len(nums):
        i = i - len(nums)
    print(i)
    print(nums)
print(nums)
#0 1 2 3 4 5 6 7 8 9 10. 11 12 13 14