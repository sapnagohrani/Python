def selection_sort(array):
    for i in range(len(array)):
        index_min_value = i
        for j in range(i+1, len(array)):
            if array[index_min_value] > array[j]:
                index_min_value = j
        array[i], array[index_min_value] = array[index_min_value], array[i]
    return array


arr = [-8, 100, 25, 50, 11, 1, 0]
print(selection_sort(arr))
