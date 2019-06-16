
from timsort import sort_a, timsort


def test_sort_a():
    s = sort_a()
    s.foo()
    assert(True)

def test_timsort():
    timsort([2, 3, 1, 5, 6, 7])