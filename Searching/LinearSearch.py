def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


array = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
key = 110
index = linear_search(array, key)
print(index) if index != -1 else print('Value Not found')
