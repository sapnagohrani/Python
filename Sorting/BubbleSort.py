def bubble_sort(array):
    for i in range(len(array)):
        swap = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
        if not swap:
            break
    return array


arr = [-8, 100, 25, 50, 11, 1, 0]
print(bubble_sort(arr))
