class HashTable:
    def __init__(self, hash_table, key, value):
        self.hash_table = hash_table
        self.key = key
        self.value = value

    def create_hash(self):  # Will return index corresponding key
        return self.key % 10

    def create_hash_table(self):
        self.hash_table[self.create_hash()].append(self.value)


if __name__ == '__main__':
    table = [[] for _ in range(10)]
    print('Empty hash table - ' + str(table))
    ht = HashTable(table, 1278, 'Dog')
    ht.create_hash_table()
    print('Hash table after adding element "Dog" - ' + str(table))
    ht1 = HashTable(table, 25, 'Cat')
    ht1.create_hash_table()
    print('Hash table after adding element "Cat" - ' + str(table))
    ht2 = HashTable(table, 335, 'Lion')
    ht2.create_hash_table()
    print('Hash table after adding element "Lion" having same position as "cat" - ' + str(table))
