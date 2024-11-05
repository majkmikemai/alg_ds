class Pair:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val


class Hashmap:
    def __init__(self) -> None:
        self.capacity = 2
        self.size = 0
        self.map = [None, None]

    def hash(self, key):
        index = 0
        for k in key:
            index += ord(k)
        return index % self.capacity

    def get(self, key):
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            else:
                index += 1
                index % self.capacity
        return None

    def put(self, key, val):
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1

                if self.capacity // 2 <= self.size:
                    self.rehash()
                return

            elif self.map[index].key == key:
                self.map[index].val = val
                return

            index += 1
            index % self.capacity

    def rehash(self):
        self.capacity = self.capacity * 2
        newMap = []

        for _ in range(self.capacity):
            newMap.append(None)

        self.map, oldMap, self.size = newMap, self.map, 0

        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)
