# 기본 인수값
# default 값을 지정해서 넣어주었으며 실제 함수 사용 시 다른 값을 입력하면 default 대신 입력된 값이 파라미터값으로 넘어감

def incr(a, step=1):
    return a + step

print(incr(10))
print(incr(10, 2))

# default값을 지정해줄 때는 생략해도 되는 값인 지 헷갈리므로 필수 파라미터 뒤 쪽으로 default값을 설정해야만 한다.

# def decr(step=-1, a):
#     return a + step

# 마찬가지로 default값은 필수 파라미터의 뒤 쪽으로 이동해야 한다.
# def decr(a, step=-1, s):
#     return a + step

def decr(a, s, step=-1):
    return a + step

# 키워드 인수
def area(width, height):
    return width * height

print(area(10,20))
print(area(width=10, height=20))
print(area(height=20, width=10))

# 오류, 위치가 맞도록, 파라미터는 중복되지 않게 해야함. 알아서 다 잡아주지 않음!!
# area(10, width=10)
# area(height=10, 10)


# 가변 인수
def vargs(a, *args):

    print(a, args, type(a), type(args))

vargs(10)
vargs(10, 102, 10, 'asd')


# print 함수 구현
def _print(*args, end='new line', sep=' '):
    print(args, end=end, sep=sep)

_print(10, 20, 30, end='tap')


# 정의되지 않은 키워드 인수 처리하기
def f(width, height, **kw):
    print(width, height)
    print(kw)

f(10, 20, depth=10, dimension=3)

# 사전 키워드 인수는  함수의 인수중에 제일 마지막에 있어야 한다.
def g(a, b, *args, **kw):
    print(a, b)
    print(args)
    print(kw)
g(10, 20, 30, 40, 50, c=60, d=70)


# 튜플/사전 파라미터
def h(name, age, height):
    print(name, age, height)

h('둘리', 10, 150)

t = ('둘리', 10, 50)

# 중요! tuple로 값을 넣어서 파라미터로 넘길 시 * 를 꼭 넣어주어야 함
h(*t)

d = {'name':'둘리', 'age': 10, 'height':150}
h(**d)
