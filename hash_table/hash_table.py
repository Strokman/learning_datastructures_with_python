

class HashTable:

    def __init__(self, size=7):
        self.data_map = size

    @property
    def data_map(self):
        return self.__data_map

    @data_map.setter
    def data_map(self, size):
        if isinstance(int(size), int):
            size = int(size)
            self.__data_map = [None] * size
        else:
            raise ValueError("Not an integer")

    def __hash(self, key):
        if isinstance(key, (int, str, float)):
            hash_value = 0
            for char in str(key):
                hash_value = (hash_value + ord(char) * 23) % len(self)
            return hash_value
        else:
            raise KeyError('Key is not hashable')

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                self.data_map[index][i][1] = value
                return
        self.data_map[index].append([key, value])

    def get(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for item in self.data_map[index]:
                if key in item:
                    return item[1]
        return None

    def keys(self):
        keys = []
        for item in self.data_map:
            if item is not None:
                for pair in item:
                    keys.append(pair[0])
        return keys

    def __len__(self):
        return len(self.data_map)

    def __str__(self):
        return f'{self.data_map}'

    def __iter__(self):
        for i in self.data_map:
            if i is not None:
                for j in i:
                    yield j[0]
