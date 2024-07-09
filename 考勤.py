n = int(input())
i = 0
answers = []
while i < n:
    s = input().split()
    answer = 'true'
    for j in range(len(s)):
        if s[j] == 'present':
            continue
        elif s[j] == 'absent':
            answer = 'false'
            break
        elif s[j] == 'late' or s[j] == 'leaveearly':#出现一个迟到早退
            if j < len(s)-1:
                if s[j+1] == 'late' or s[j+1] == 'leaveearly' :#是否连续
                    answer = 'false'
                    break
                else:
                    continue
            else:
                continue
    answers.append(answer)
    i+=1
for k in answers:
    print(k,end=' ')