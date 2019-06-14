def dummy():
    pass

def my_function():
    print('Hello World')

def times(a, b):
    return a * b

def none():
    return

def my_function2(func):
    func()

dummy()
my_function()
print(times(10, 10))
print(none())

print(dummy, type(dummy))

f = my_function

print(f, my_function)

# 여러 return 값
def func():
    return 10, 'hello', {1, 2, 3}, (1, 2, 3)

십, 헬로우, 셋, 튜플 = func()

print(십, 헬로우, 셋, 튜플)

