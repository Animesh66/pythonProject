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


test_yield()
test_return()
