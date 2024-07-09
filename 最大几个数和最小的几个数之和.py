#数组长度输入
M = int(input())
#数组内容输入
nums_str = input().split(' ')
nums = list(map(int,nums_str))
nums = sorted(set(nums))
#N输入
N = int(input())
if len(nums) < N*2:
    exit(-1)
sum = 0
for i in range(N):
    sum = sum + nums[i] + nums[-1-i]
print(sum)
