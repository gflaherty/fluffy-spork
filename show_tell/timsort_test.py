
from timsort import timsort
from timsort_b import timsort as timsort_b
from timsort_c import timsort as timsort_c

def test_timsort():
    ret = timsort([2, 3, 1, 5, 6, 7])
    assert(ret == sorted(ret))

def test_timsort_b():
    ret = timsort_b([1, 2, 3, 5, 6, 7])
    assert(ret == sorted(ret))

def test_timsort_c():
    ret = timsort_c([7, 6, 5, 4, 3, 2, 1])
    assert(ret == sorted(ret))
