n = input()

codes = [
    ['a','1'],
    ['b','2'],
    ['c','3'],
    ['d','4*'],
    ['e','5*']
]
answer = ''
i = 0
while i < len(n):
    if i < len(n)-1:#不是最后一个
        if n[i+1] == '*':
            for j in range(3,len(codes)):
                if n[i]+'*' == codes[j][1]:
                    answer = answer + codes[j][0]
                    i+=1
                    break
        else:
            for k in range(0,3):
                if n[i] == codes[k][1]:
                    answer = answer + codes[k][0]
                    break
    else:
        for l in range(0, 3):
            if n[i] == codes[l][1]:
                answer = answer + codes[l][0]
                break
    i+=1
print(answer)