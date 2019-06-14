# lamda 예약어를 사용해서 정의하며, ‘익명 함수를 선언한다’라는 의미이다.
# 데이터 분석/변형 함수에서 파라미터로 해당 처리 함수를 인자로 받는 경우가 많다.(사용 빈도가 높다)

def f(x):
    return x * 2

for i in range(10):
    print('{0}*2={1},'.format(i, f(i)), end=' ')
else:
    print()

# 함수를 람다로 변경
# lambda 로 함수를 정의하고 f 자리에 대체하기
for i in range(10):
    print('{0}*2={1},'.format(i, (lambda x: x*2)(i)), end=' ')
else:
    print()
