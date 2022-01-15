class testsum:
    def __init__(self):
        '이 class는 시험 점수의 합과 평균을 계산해 줍니다.'

    def file_write(self):
        line = ['100\n', '90\n', '89\n', '88\n', '100\n']
        with open('../student_grades.txt', 'r')as file:
            file.writelines(line)

    def file_read(self):  # 파일의 값을 배열로 리턴하는 함수
        h = []
        with open('../cls/student_grades.txt', 'r')as file:
            line = None
            while line != '':
                line = file.readline()
                a = line.strip('\n')
                if (a != ''):
                    h.append(int(a))
        return h

    def file_print(self, list):  # 파일의 값들의 합과 편균 구하는 함수
        x = 0
        for i in list:
            x = x + i
        print('시험 점수의 총합', x, '시험 점수의 평균', x / len(list))
