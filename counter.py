def createcounter():
    c = 0
    def counter():
        nonlocal c
        c += 1
        return c
    return counter


counterA= createcounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())


counterB = createcounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')