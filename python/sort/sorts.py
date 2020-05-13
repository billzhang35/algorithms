#!/usr/bin/env python
import timeit
import python.sort.utils as utils
from random import randint

# 冒泡排序
# 比较相邻两项，并交换错序的项
def bubble_sort(array):
    n = len(array)
    is_swap = False
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_swap = True
        if not is_swap:
            break
    return array


# 选择排序
# 选出最小元素，交换到当前位置
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_pos = i
        for j in range(i + 1, n):
            if array[j] < array[min_pos]:
                min_pos = j
        array[i], array[min_pos] = array[min_pos], array[i]
    return array


# 插入排序
# 将第i+1个元素，插入到前i个元素中的正确位置
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        cur_val = array[i]
        pos = i
        while array[pos - 1] > cur_val and pos > 0:
            array[pos] = array[pos - 1]
            pos -= 1
        array[pos] = cur_val
    return array


# 希尔排序
#
def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap):
            insertion_sort_by_gap(array, i, gap)
        gap //= 2
    return array


def insertion_sort_by_gap(array, start_pos, gap):
    n = len(array)
    for i in range(start_pos + gap, n, gap):
        cur_val = array[i]
        pos = i
        while array[pos - gap] > cur_val and pos > 0:
            array[pos] = array[pos - gap]
            pos -= gap
        array[pos] = cur_val
    return array


# 归并排序
def merge_sort(array):
    return __merge_sort(array, 0, len(array) - 1)


def __merge_sort(array, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    __merge_sort(array, start, mid)
    __merge_sort(array, mid + 1, end)
    if array[mid] > array[mid + 1]:
        merge_sorted_array(array, start, mid, end)


# 归并排序好的数组 [start, ..., mid] [mid+1, ..., end]
def merge_sorted_array(array, start, mid, end):
    temp_array = array[start: end + 1]
    p_mid = mid - start
    p_end = end - start
    p1 = 0
    p2 = p_mid + 1
    pos = start
    while pos <= end:
        if p1 > p_mid:
            array[pos] = temp_array[p2]
            p2 += 1
        elif p2 > p_end:
            array[pos] = temp_array[p1]
            p1 += 1
        elif temp_array[p1] <= temp_array[p2]:
            array[pos] = temp_array[p1]
            p1 += 1
        else:
            array[pos] = temp_array[p2]
            p2 += 1
        pos += 1
    return array


def merge_sort_non_recursive(array):
    n = len(array)
    step = 1
    while step < n:
        for i in range(0, n - step, step * 2):
            start = i
            end = min(i + step * 2 - 1, n - 1)
            mid = i + step - 1
            merge_sorted_array(array, start, mid, end)
        step *= 2
    return array


def merge_sort_linked_list(head):
    pass


def quick_sort(array):
    return __quick_sort(array, 0, len(array) - 1)


def __quick_sort(array, start, end):
    if start >= end:
        return
    pivot = partition(array, start, end)
    __quick_sort(array, start, pivot - 1)
    __quick_sort(array, pivot + 1, end)
    return array


def partition(array, start, end):
    # i遍历数组，j卡住分界点，最后再跟首位的分界值互换
    pos = randint(start, end)
    val = array[pos]
    array[start], array[pos] = array[pos], array[start]
    i = start + 1
    j = start
    while i <= end:
        if array[i] < val:
            array[i], array[j + 1] = array[j + 1], array[i]
            j += 1
        i += 1
    array[start], array[j] = array[j], array[start]
    return j




if __name__ == '__main__':
    #t1 = timeit.Timer
    alist = utils.generate_random_array(10, 0, 100)
    print(alist)
    res = quick_sort(alist)
    #res = insertion_sort_by_gap(alist, 0, 3)
    #res = merge_sorted_array(alist, 0, 2, 4)
    print(utils.is_sorted(res))
    print(res)






