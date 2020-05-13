#!/usr/bin/env python
from random import randint


class Node(object):
    def __init__(self, val=None, next_node=None):
        self.value = val
        self.next = next_node


def generate_random_array(n, min_num, max_num):
    return [randint(min_num, max_num) for i in range(n)]


def generate_random_linked_list_by_array(array):
    next_node = None
    for i in range(len(array)-1, -1, -1):
        cur_node = Node(array[i], next_node)
        next_node = cur_node
    return next_node


def generate_random_linked_list(n, min_num, max_num):
    next_node = None
    for i in range(n):
        cur_node = Node(randint(min_num, max_num), next_node)
        next_node = cur_node
    return next_node


def print_linked_list(head):
    result = str(head.value)
    cur_node = head.next
    while cur_node is not None:
        result += "->" + str(cur_node.value)
        cur_node = cur_node.next
    print(result)


def generate_nearly_ordered_array(n, swap_times):
    array = [i for i in range(n)]
    for j in range(swap_times):
        x = randint(0, n - 1)
        y = randint(0, n - 1)
        array[x], array[y] = array[y], array[x]
    return array


def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True


if __name__ == '__main__':
    list_a = generate_random_array(10, 0, 100)
    #head_a = generate_random_linked_list(10, 0, 100)
    head_a = generate_random_linked_list_by_array(list_a)
    print(list_a)
    print(head_a.value)
    print_linked_list(head_a)

