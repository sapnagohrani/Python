def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]
        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0
        while len(left_array) > i and len(right_array) > j:
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        while len(left_array) > i:
            array[k] = left_array[i]
            i += 1
            k += 1
        while len(right_array) > j:
            array[k] = right_array[j]
            j += 1
            k += 1


def print_array(array):
    print(array)


if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]
    merge_sort(array)
    print('After Sorting : ' + str(array))
