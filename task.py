from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
    if not container:
        return container

    def quicksort(alist, start, end):
        if start < end:
            p = partition(alist, start, end)
            quicksort(alist, start, p)
            quicksort(alist, p + 1, end)

    quicksort(container, 0, len(container) - 1)
    return container


def partition(alist, start, end):
    pivot = alist[(start+end) // 2]
    i = start
    j = end
    while i <= j:
        while alist[i] < pivot:
            i += 1
        while alist[j] > pivot:
            j -= 1
        if i >= j:
            break
        alist[i], alist[j] = alist[j], alist[i]
        i += 1
        j -= 1
    return j



# def partition(container, i, j):
#     pivot = container[len(container) // 2]
#     while i <= j:
#         while container[i] <= pivot:
#             i += 1
#         while container[j] >= pivot:
#             j -= 1
#         if i <= j:
#             container[i], container[j] = container[j], container[i]
#             i += 1
#             j -= 1
#         else:
#             break
#     return i


# a = [51, 95, 66, 72, 42, 38, 39, 41, 15]
# print(partition(a, 0, 8))
# print(a)
#
# a = [40, 95, 66, 72, 42, 38, 39, 41, 15]
# print(partition(a, 0, 8))
# print(a)
#
# print(sort([40, 95, 66, 72, 42, 38, 39, 41, 15]))