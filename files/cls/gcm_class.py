class greatest_common_factor:
    def __init__(self):
        print('이 프로그램은 두개의 수(n개의 수)를 받아서, 그 수들의 최대공약수를 찾아주는 프로그램 입니다.')

    def two_numders(self, x, y):
        h = []
        i = 2
        if x >= y:
            a = x
        elif y > x:
            a = y
        while i <= a:
            if x % i == 0 and y % i == 0:
                h.append(i)
            i = i + 1
        return h

    def max_numders(self, h):
        h.sort(reverse=True)
        v = h[0]
        return v
