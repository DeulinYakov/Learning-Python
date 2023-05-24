def foo(data, *, start=0, end=1000):
    for value in (data[start:end]):
        print(value)


def foo2():
    """sklajdfjsa"""
    print(1)


# print(foo2, __doc__)
# print("=====================")
# print(help(foo2))

def add(arg1, arg2):
    return arg1 + arg2


def run(func, a, b):
    if callable(func):
        res = func(a, b)
    else:
        res = None
    return res


def outer(a, b):
    def inner(c, d):
        return c + d

    return inner(a, b)
