import time,functools
def metric(func):
    @functools.wraps(func)
    def wrapper(*arg):
        start_time = time.time()
        print('%s executed in %s ms' % (func.__name__,time.time()-start_time ))
        return func(*arg)
    return wrapper


@metric
def fast(x, y):
    print(x + y)

print(fast(1,2))
