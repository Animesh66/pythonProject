def test_yield():
    print("test yield started")
    yield 1
    print("test yield ended")
    yield 2
    print("another yield")


def test_return():
    print("test return started")
    return 3
    print("test return ended")


yield_value = test_yield()
return_value = test_return()
print(list(yield_value))
print(return_value)