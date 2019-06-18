
from timsort import timsort
from timsort_a import timsort as timsort_a
from timsort_b import timsort as timsort_b
from timsort_c import timsort as timsort_c
from timsort_d import timsort as timsort_d
import random

arr = (2, 3, 1, 5, 6, 7)
arr_a = (1, 2, 3, 4, 1, 2, 3, 4)
arr_b = (1, 1, 1, 1, 1)
arr_c = (7, 6, 5, 4, 3, 2, 1)
arr_d = (1, 1, 1, 1, 0)
# arr_d = (1, 1, 3, 3, 0, 0)
arr_d = [4, 5, 7, 2, 8, 7, 10, 3]# + list(arr_c)
#random.shuffle(arr_d)
# arr_d = []
# for i in range(5):
#     arr_d.append(random.randint(1, 25))
# print("foo")
# print(arr_d)

def test_timsort():
    ret = timsort(arr)
    assert(ret == sorted(arr))

def test_timsort_a():
    ret = timsort_a(arr)
    assert(ret == sorted(arr))
    ret = timsort_a(arr_a)
    assert(ret == sorted(arr_a))

def test_timsort_b():
    ret = timsort_b(arr)
    assert(ret == sorted(arr))
    ret = timsort_b(arr_a)
    assert(ret == sorted(arr_a))
    ret = timsort_b(arr_b)
    assert(ret == sorted(arr_b))

def test_timsort_c():
    ret = timsort_c(arr)
    assert(ret == sorted(arr))
    ret = timsort_c(arr_a)
    assert(ret == sorted(arr_a))
    ret = timsort_c(arr_b)
    assert(ret == sorted(arr_b))
    ret = timsort_c(arr_c)
    assert(ret == sorted(arr_c))

def test_timsort_d():
    ret = timsort_d(arr)
    assert(ret == sorted(arr))
    ret = timsort_d(arr_a)
    assert(ret == sorted(arr_a))
    ret = timsort_d(arr_b)
    assert(ret == sorted(arr_b))
    ret = timsort_d(arr_c)
    assert(ret == sorted(arr_c))
    ret = timsort_d(arr_d)
    assert(ret == sorted(arr_d))
