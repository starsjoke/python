answer = 5
problems=['sin', 'cos', 'acrtan', 'sec', 'css']
pick = 0
print('다음중 삼각함수가 아닌 함수를 고르시요1.',problems)
while pick != answer:
    pick = int(input('1부터 5중에 정답이라고 생각하는 답안 입력'))
    if pick == answer:
        print('정답입니다.')
        break
    else:
        continue
