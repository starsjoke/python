import files.cls.gcm_class as cls
shkey=cls.greatest_common_factor()
a=int(input('정수를 입력하시오: '))
b=int(input('정수를 입력하시오: '))
x=shkey.two_numders(a,b)
y=shkey.max_numders(x)
print('두 수',a,b,'의 공약수는 :',x)
print('두 수',a,b,'의 최대 공약수는 :',y)