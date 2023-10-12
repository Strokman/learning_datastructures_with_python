

class HashTable:

    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value + ord(char) * 23) % len(self)

    def __len__(self):
        return len(self.data_map)

    def __str__(self):
        return f'{self.data_map}'