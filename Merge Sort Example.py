__author__ = 'Jun'

# Just an implementation of merge sort in Python


def merge_sort(unsorted_list):
    n = len(unsorted_list)

    if n == 1:
        return unsorted_list

    first_half = unsorted_list[0:n // 2]
    second_half = unsorted_list[n // 2:n]

    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)

    return merge(first_half, second_half)


def merge(list_one, list_two):
    size_1 = len(list_one)
    size_2 = len(list_two)
    i = 0
    j = 0
    k = 0

    merged_list = []
    while i < size_1 and j < size_2:
        if list_one[i] <= list_two[j]:
            merged_list.append(list_one[i])
            i += 1
        else:
            merged_list.append(list_two[j])
            j += 1
        k += 1

    if i < size_1:
        merged_list.extend(list_one[i:size_1])
    else:
        merged_list.extend(list_two[j:size_2])

    return merged_list