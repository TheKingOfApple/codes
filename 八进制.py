
n = int(input())
luck = int(input())
m = int(input())
answer = []
def C8QY(number):
    print(number)
    answer.append(number%8)
    if number/m == 0:
        return
    else:
        C8QY(int(number/m))
C8QY(n)
sum = 0
for i in answer:
    if luck == i:
        sum += 1
print(answer)
print(sum)