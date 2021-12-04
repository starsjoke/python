def resoving(answer):
    while pick != answer:
        pick = int(input('1부터 5중에 정답이라고 생각하는 답안 입력'))
        if pick == answer:
            print('정답입니다.')
            break
        else:
            continue
            return pick