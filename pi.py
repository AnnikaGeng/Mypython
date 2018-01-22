import itertools
def pi(N):
    odd = itertools.count(1,2)
    ini = itertools.takewhile(lambda x: x <= 2*N-1, odd)
    position = 1
    result = 0
    for n in ini:
        if position % 2 == 1:
            result = result + (4.0/n)
        else:
            result = result - (4.0/n)
        position += 1
    return result


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')