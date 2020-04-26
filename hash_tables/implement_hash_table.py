class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        my_hash = 0
        for i in range(len(key)):
            my_hash = (my_hash + ord(key[i]) * i) % len(self.data)
        return my_hash

    def set(self, key, value):
        address = self._hash(key)
        if self.data[address] is None:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        if current_bucket:
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    print(current_bucket[i][1])
                    return current_bucket[i][1]
        return None

    def keys(self):
        keys = [key[0][0] for key in self.data if key]
        print(keys)
        return keys


hash_table = HashTable(50)
hash_table.set('grapes', 100000)
hash_table.get('grapes')
hash_table.set('apples', 9)
hash_table.get('apples')
hash_table.set('oranges', 500)
hash_table.keys()

