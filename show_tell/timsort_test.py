
from timsort import timsort
from timsort_a import timsort as timsort_a
from timsort_b import timsort as timsort_b
from timsort_c import timsort as timsort_c
from timsort_d import timsort as timsort_d

arr = [2, 3, 1, 5, 6, 7]
arr_a = [7, 1, 2, 3, 4, 5]
arr_b = [1, 2, 3, 5, 6, 7]
arr_c = [7, 6, 5, 4, 3, 2, 1]
arr_d = [6, 7, 5, 4, 3, 2, 1]

def test_timsort():
    ret = timsort(arr)
    assert(ret == sorted(ret))

def test_timsort_a():
    ret = timsort_a(arr)
    assert(ret == sorted(ret))
    ret = timsort_a(arr_a)
    assert(ret == sorted(ret))

def test_timsort_b():
    ret = timsort_b(arr)
    assert(ret == sorted(ret))
    ret = timsort_b(arr_a)
    assert(ret == sorted(ret))
    ret = timsort_b(arr_b)
    assert(ret == sorted(ret))

def test_timsort_c():
    ret = timsort_c(arr)
    assert(ret == sorted(ret))
    ret = timsort_c(arr_a)
    assert(ret == sorted(ret))
    ret = timsort_c(arr_b)
    assert(ret == sorted(ret))
    ret = timsort_c(arr_c)
    assert(ret == sorted(ret))

def test_timsort_d():
    ret = timsort_d(arr)
    assert(ret == sorted(ret))
    ret = timsort_d(arr_a)
    assert(ret == sorted(ret))
    ret = timsort_d(arr_b)
    assert(ret == sorted(ret))
    ret = timsort_d(arr_c)
    assert(ret == sorted(ret))
    ret = timsort_d(arr_d)
    assert(ret == sorted(ret))
