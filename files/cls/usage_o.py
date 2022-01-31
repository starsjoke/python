class testsum:
    def __init__(self):
        '이 class는 시험 점수의 합과 평균을 계산해 줍니다.'

    def file_read(self):  # 파일의 값을 배열로 리턴하는 함수
        mt = []
        ko = []
        with open('./student_grades.txt', 'r') as file:
            line = None
            while line != '':
                line = file.readline()
                a = line.strip('\n')
                if (a != ''):
                    tmp = a.split(',')
                mt.append(tmp[0])
                ko.append(tmp[1])
        return mt, ko

    def file_print(self, ko, mt):  # 파일의 값들의 합과 편균 구하는 함수
        x = 0
        y = 0
        for i in ko:
            x = x + int(i)
        for j in mt:
            y = y + int(j)
        print('국어 점수의 총합', x, '국어 점수의 평균', x / len(ko), '수학 점수의 총합', y, '수학 점수의 평균', y / len(mt))
