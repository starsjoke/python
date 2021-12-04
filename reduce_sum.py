from functools import reduce

p = input('숫자 입력하세리어미;ㅓ럼ㄴ라ㅣㅓ : ')
im = map(float, p.split(','))
imlist = list(im)
jl = filter(lambda x: x % 2 == 0, imlist)
im_2nlist = list(jl)

ln=len(im_2nlist)
if ln == 0:
    sum1=0
else :
   sum1 = reduce(lambda x, y: x + y, im_2nlist)


print('sum=', sum1)


