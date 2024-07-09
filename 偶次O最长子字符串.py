n = input()
o_num = 0
#反向思考，从o最多的开始减，只有奇数和偶数两种情况，偶数原字符串就是最长子字符串，奇数挑一个o出来，又因为首尾相联，此时最长子字符串长度为len(n)-1
for i in n:
    if i == 'o':
        o_num+=1
if o_num%2 == 0:#偶数
    print(len(n))
else:
    print(len(n)-1)
print('字符串原长',len(n))