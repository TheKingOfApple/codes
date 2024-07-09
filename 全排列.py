n = [1,2,3,4,5]
answer = []
i_number = []
stop = 1
sums = 0
for s in range(1,len(n)+1):
    stop*=s
print(stop)
num=[0]*len(n)
def DG(n,x=0):
    for i in range(x,len(n)):
        num[x] = n[i]
        print('i=',i,'x=',x)
        if x == len(n)-1:
            answer.append(num)
            return
        else:
            DG(n,x+1)
    return answer
print(DG(n))