# -*- coding: utf-8 -*-

def partition(num_list, left, right):
    temp = num_list[left]
    while left < right:
        while left < right and num_list[right] >= temp:
            right -= 1
        num_list[left], num_list[right] = num_list[right], num_list[left]
        while left < right and num_list[left] <=  temp:
            left += 1
        num_list[left], num_list[right] = num_list[right], num_list[left]
    return left

def quick_sort(num_list, left, right):
    if left < right:
        pivot = partition(num_list, left, right)
        quick_sort(num_list, left, pivot-1)
        quick_sort(num_list, pivot+1, right)
    return num_list

if __name__ == "__main__":
    num_list = [1,1,23,34,1,2,3,1,4,2,6,3]
    left = 0
    right = len(num_list) - 1
    print(quick_sort(num_list, left, right))
