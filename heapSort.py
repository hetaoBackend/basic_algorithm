# -*- coding: utf-8 -*-

def heapCreate(num_list, size):
    a = size//2 - 1
    while a >= 0:
        heapAdjust(num_list, a, size)
        a -= 1

def heapAdjust(num_list, i, size):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    max_temp = i
    if left_child < size and num_list[left_child] < num_list[max_temp]:
        max_temp = left_child
    if right_child < size and num_list[right_child] < num_list[max_temp]:
        max_temp = right_child
    if max_temp != i:
        num_list[i], num_list[max_temp] = num_list[max_temp], num_list[i]
        heapAdjust(num_list, max_temp, size)

def heapSort(num_list):
    result = []
    while num_list:
        size = len(num_list)
        heapCreate(num_list, size)
        result.append(num_list.pop(0))
    return result

if __name__ == "__main__":
    num_list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print(heapSort(num_list))
