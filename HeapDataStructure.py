class HeapDS:
    def __init__(self, array):
        self.array = array
        self.size = (len(array)) // 2  # Remaining half elements of a list become leaf nodes

    def do_swap(self, i):
        # Logic to create Heap data structure from list
        if self.array[i] > self.array[2 * i + 1]:
            if self.array[2 * i + 2] and self.array[2 * i + 2] > self.array[2 * i + 1]:
                self.array[i], self.array[2 * i + 1] = self.array[2 * i + 1], self.array[i]
                if (2 * i + 1) < self.size:
                    self.do_swap(2 * i + 1)  # Left node needs to be revisit if left swap happens
            else:
                self.array[i], self.array[2 * i + 2] = self.array[2 * i + 2], self.array[i]
                if (2 * i + 2) < self.size:
                    self.do_swap(2 * i + 2)  # Right node needs to be revisit if right swap happens

    def create_heap_ds(self):
        print(self.array)
        # Right half of the list elements become Leaf Nodes in a binary tree
        for i in range(self.size - 1, 0, -1):
            self.do_swap(i)

    def print_heap_ds(self):
        print(self.array)


if __name__ == '__main__':
    heap = HeapDS([1, 9, 8, 2, 3, 10, 14, 7, 16, 4])
    heap.create_heap_ds()
    heap.print_heap_ds()
