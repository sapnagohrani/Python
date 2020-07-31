def binary_search(array, key, low, high):
    if array != sorted(array):
        print('List should be sorted')
        return -1
    if high>=low:
        mid = (low + high) // 2
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            return binary_search(array, key, mid + 1, high)
        else:
            return binary_search(array, key, low, mid - 1)
    else:
        return -1


array = [10, 20, 30, 50, 60, 80, 100, 110, 130, 170]
key = 110
index = binary_search(array, key, 0, len(array) - 1)
print(index) if index != -1 else print('Value Not found')
