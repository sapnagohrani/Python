arr = [-8, 100, 25, 50, 11, 1, 0]


def insertion_sort(array):
    for i in array:
        j = array.index(i)
        while j > 0:
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
            j = j - 1
    return array


print(insertion_sort(arr))
