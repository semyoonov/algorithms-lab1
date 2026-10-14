import random
from algorithms.binary_search import binary_search
from algorithms.double_binary_search import double_binary_search
from algorithms.exponential_search import exponential_search
from algorithms.two_pointers import two_pointers

def generate_sample(m=None, n=None, has_common=None):
    if m is None and n is None:
        n = random.randint(1, 10)
        m = n
    elif m is None:
        m = n
    elif n is None:
        n = m

    if has_common is None:
        has_common = random.randint(0, 1)

    a = [2 * int(i * n / m) + 1 for i in range(m)]
    b = [2 * i for i in range(n)]

    if has_common and m > 0 and n > 0:
        idx_a = random.randint(0, m - 1)
        idx_b = random.randint(0, n - 1)
        a[idx_a] = b[idx_b]
        a.sort()

    return a, b, bool(has_common)


def test_binary_search():
    a, b, has_common = generate_sample()
    print(a)
    print(b)

    res = binary_search(a, b)
    print(res)
    assert res == has_common

def test_double_binary_search():
    a, b, has_common = generate_sample()
    print(a)
    print(b)

    res = double_binary_search(a, b)
    print(res)
    assert res == has_common

def test_exponential_search():
    a, b, has_common = generate_sample()
    print(a)
    print(b)

    res = exponential_search(a, b)
    print(res)
    assert res == has_common

def test_two_pointers():
    a, b, has_common = generate_sample()
    print(a)
    print(b)

    res = two_pointers(a, b)
    print(res)
    assert res == has_common