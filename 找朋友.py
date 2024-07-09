#123 124 125 121 119 122 126 123
#输入
M = int(input())
nums = list(map(int,input().split()))
#定义一个全为0长度为M的数组，这样后面用lit[i]=方法修改就行了
answer = [0 for i in range(M)]
#找，用遍历数组的方法找
for i in range(M):
    j = i+1
    tip = False
    #看一下第i个小朋友前面所有的小朋友
    while j < M:
        if nums[i] < nums[j]:
            answer[i] = j
            tip = True
        print(i,j)
        j+=1
        #找到第一个比他高的就结束while循环
        if tip == True:
            print('tip')
            break
print(answer)
