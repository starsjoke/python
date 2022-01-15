# lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
# with open('hello.txt', 'w') as file:
#     file.writelines(lines)
with open('hello.txt', 'r')as file:
   # lines = file.readlines()
    #print(lines)
    line=None
    while line !='':
        line=file.readline()
        print(line.strip('\n'))