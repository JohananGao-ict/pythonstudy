from functools import reduce
origin = 0
def curve_pre():
    a = 250
    def curve(x):
        return a*x*x
    return curve

def go(step):
    global origin  #全局变量
    origin = new_pos = origin + step
    return new_pos

def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos +step
        pos = new_pos
        return new_pos
    return go

f1 = lambda x,y: x+y
print(f1(1,2))
#三元表达式  xx？x：x
x = 1
y = 2
r = x if x > y else y

f=curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))
print(curve_pre()(2))  #ok

print(go(2))
print(go(4))
print(go(6))
print('==============')

tourist = factory(origin)
print(tourist(2))
print(tourist(2))
print(tourist(2))
print(tourist(2))


map()