numbers = input()
answers = [[]]
#递归遍历出所有结果
s_number = numbers#读入数据使用
i_number = []#当次组合
def section(number:list): 
    for i in 0,-1:
        i_number.append(number[i])
        del number[i]
        if len(number) > 0:
            section(number)
        else:
            