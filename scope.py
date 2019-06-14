# (L)GB
def func(a):
    x = 2
    return a + x
# SCOPE  L : LOCAL , G = GLOBAL, B = BULIT IN
print(func(10))

# L(G)B
x = 1
def func2(a):
    x = 2
    return a + x

print(func2(10))
print(x)

# LOCAL의 변수를 GLOBAL에서 가져오기
g = 1
def func3(a):
    global g
    g = 3
    return a + g
print('g =',g)
print('func3 =', func3(10))
print('g =',g)

# LG(B)
print(dir('__bulitins__'))

