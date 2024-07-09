names = []
hands = []
while True:
    shuru = input()
    if shuru == '':
        break
    names.append(shuru[:-2])
    hands.append(shuru[-1])
A = []
B = []
C = []
for i in range(len(hands)):
    if hands[i] == 'A':
        A.append(names[i])
    elif hands[i] == 'B':
        B.append(names[i])
    elif hands[i] == 'C':
        C.append(names[i])
if len(A) > 0 and len(B) > 0 and len(C) > 0:
    print('NULL')
elif len(C) == 0 and len(B) > 0 and len(A) >0:
    print(A)
elif len(A) > 0 and len(B) == 0 and len(C) > 0:
    print(C)
elif len(A) == 0 and len(B) > 0 and len(C) > 0:
    print(A)
else:
    print('NULL')