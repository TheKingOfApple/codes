s = input()
l = input()
if len(s) > len(l):
    exit(0)
tap = 0
stop = False
for j in s:
    for i in range(tap,len(l)):
        if l[i] == j:
            print('找到',l[i])
            tap = i+1
            break
        if i+1 == len(l):
            stop = True
    if stop == True:
        print('不是')
        break
    elif stop == False and j == s[-1]:
        print('是')