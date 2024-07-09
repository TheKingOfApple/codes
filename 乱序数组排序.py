n = input().split()

nums = []
s = []#查重存储数组
#去重并记录出现次数
for i in n:#遍历输入的数据
    if len(nums) > 0:#非第一个数据
        if i in s:#如果重复
            for j in nums:#找到重复的数据存在哪
                if j['name'] == i:
                    j['sum'] += 1#出现次数加一
                    break
        else:#不重复
            nums.append({'name':i,'sum':1})
            s.append(i)
    else:#第一个数据
        nums.append({'name': i, 'sum': 1})
        s.append(i)
#排序
temp = sorted(nums,key = lambda i:i['sum'],reverse=True)
answer = []
for i in temp:
    answer.append(i['name'])
print(nums)
print(answer)