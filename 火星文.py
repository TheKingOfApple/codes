#用栈实现中缀表达式计算
nums = []#存数字
sign = []#存符号

def cul_1(a,b):##的计算
    a = int(a)
    b = int(b)
    return 4*a+3*b+2

def cul_2(a,b):#$的计算
    a = int(a)
    b = int(b)
    return 2*a+b+3

s = input()
i = 0
while i <len(s):
    num = ''
    if s[i] == '#':
        k = i+1
        while s[k] != '#' and s[k] != '$':
            num = num+s[k]
            k+=1
            if k == len(s):
                break
        print(nums[-1],'和',num,'运算')
        nums[-1] = cul_1(nums[-1],num)
        i+=2
    elif s[i] == '$':
        sign.append(s[i])
    else:
        nums.append(s[i])
    i+=1
for j in range(0,len(nums),2):
    print(nums[j],nums[j+1])
    answer = cul_2(nums[j],nums[j+1])
print(answer)
print(nums)