def sum(numbers):#进行求和计算
    s_answer = 0
    for i in numbers:
        s_answer = s_answer + i
    return s_answer
need = int(input('整数为？'))
if type(need) != int or need < 3:
    print('警告！请输入不为0且大于2的整数')
    exit(0)
answers = [[]]#最终答案存储
if need % 2 == 0:
    UpLimit = need/2
else:
    UpLimit = need/2 + 1
UpLimit = int(UpLimit)
number = [UpLimit]
for i in range(UpLimit-1,0,-1):
    number.append(i)
    # print(number)
    if sum(number) == need:
        answers.append(number)
        # print(answers)
        number = number[1:]
    elif sum(number) > need:
        number = number[1:]
# print(answers)
for j in answers[1:]:
    print(need,end='')
    print('=',end='')
    for l in j[::-1]:
        print(l,end='')
        if l != j[::-1][-1]:
            print('+',end='')
    print()



