# call by reference 이지만 내부에서 변경되더라도 변경되지 않는다.(immutable)

def f(t):
    t = 20
    return t
a = 10
b = f(a)
# 함수에 a값을 넣어서 함수 내에서 변경을 시도했지만 결과적으로 변경되지 않는다.
print(a)
# 함수의 return 값으로는 변경된 값으로 변경된다. 즉 함수 내에서 사용되는 변수는 다른 참조이다.
print(b)

# 파라미터가 immutable 인 경우 내부에서 변경 시 오류가 발생하므로 주의 요망, 추후 작업이 커지면 종종 발생할 수 있음
def h(t):
    t = (10, 20, 30)
    # t[0] = 10
a = (1, 2, 3)
h(a)
print(a)

# 파라미터가 mutable인 경우에는 변경이 가능하다.
def g(t):
    t[0] = 0

a = [1, 2, 3]
g(a)
print(a)

