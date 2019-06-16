
from timsort import sort_a, timsort


def test_sort_a():
    s = sort_a()
    s.foo()
    assert(True)

def test_timsort():
    ret = timsort([2, 3, 1, 5, 6, 7])
    assert(ret == sorted(ret))
