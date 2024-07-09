#4,5,6,7,0,1,2
# innums = input().split(',')
# outnums = list(map(int,input().split(',')))
innums = [4,5,6,7,0,1,2]
outnums = [6,4,0,1,2,5,7]
#转换成从0开始的序列方便理解
outIndex = []
for j in outnums:
    for i in range(len(innums)):
        if j == innums[i]:
            outIndex.append(i)
            break

nums = [k for k in range(len(innums))]#0到n的列表

#遍历outnums，如果i不在box里，执行从nums[0]到nums[i]存入box并删除box[-1]，记录从右边取出
#如果i在box里，判断在第一个还是第二个，从box删除对应位置，并记录从哪边取出；如果不在两边就输出NO

answer = []#存答案
box = []#存入已经放入的数


def Mainway(nums:list,answer:list,outIndex:list,box:list):#主函数
    for i in outIndex:#遍历输出顺序
        if i not in box:#如果i还不在box里，就一直读入直到i进来，然后从右边取出
            j = nums[0]
            while j <= i:
                j+=1
                box.append(nums[0])
                del nums[0]
                print(i, '不在box,执行操作 box=', box, end='')
                print('nums变为', nums)
            if len(box) > 0:#判断一下是不是最后一个
                answer.append('R')
            else:
                answer.append('L')
            print('answer新增',answer)
            del box[-1]
        elif i in box:
            if i == box[0]:
                del box[0]
                print('l')
                print('box=',box)
                answer.append('L')
            elif i == box[-1]:
                del box[-1]
                print('r')
                answer.append('R')
            else:
                print(i)
                print(answer)
                print('NO')
                break
            print(i,'在box里，执行操作，box=',box)
    print(answer)

if len(outIndex) < len(outnums):#判断输出是否大于输入
    print('输入大于输出，NO')
else:
    Mainway(nums,answer,outIndex,box)