# for i in range(220,1,-1):
#     print(i)

# n = int(input())
n = 1178
# answer = 0
# for i in range(7,n,7):
#         answer = answer +1
# for j in range(7,n,10):
#     if j % 7 ==0:
#         continue
#     else:
#         # print(j)
#         answer = answer +1
# if 80 > n > 70:
#     answer = answer +n -70
# else:
#     answer = answer + 9
#
# if n > 77:
#     answer = answer -1
# print(int(answer))
answer = 0
b2 = []
for i in range(1,n):
    if i % 7 == 0:
        answer = answer +1
        b2.append(i)
    elif '7' in str(i):
        answer = answer +1
        b2.append(i)
def seven(n: int):
    num = 0
    a = []
    if n <= 6:
        return 0

    for i in range(7, n + 1):

        i_s = str(i)

        if i % 7 == 0 or '7' in i_s:
            num += 1
            a.append(i)

    return a
a = seven(n)
print(b2)
print(a)
for j in range(len(b2)):
    print(b2[j],a[j])
    if b2[j] != a[j]:
        print(11111)
        print(b2[j-3:j+3])
        print(a[j-3:j+3])