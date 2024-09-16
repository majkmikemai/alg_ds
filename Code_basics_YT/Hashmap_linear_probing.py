"""
Implement hash table where collisions are handled using linear probing.
We learnt about linear probing in the video tutorial.
Take the hash table implementation that uses chaining and modify methods to use linear probing.
Keep MAX size of arr in hashtable as 10.
"""


class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        hash = self.get_hash(key)

        start_pos = hash

        while self.arr[hash] is not None:
            if self.arr[hash][0] == key:
                self.arr[hash] = (key, value)
                return

            hash = (hash + 1) % self.MAX

            if hash == start_pos:
                raise Exception("There is no empty space left")

        self.arr[hash] = (key, value)

    def __getitem__(self, key):
        hash = self.get_hash(key)

        start_pos = hash

        while self.arr[hash] is not None:
            if self.arr[hash][0] == key:
                return self.arr[hash][1]

            hash = (hash + 1) % self.MAX

            if hash == start_pos:
                raise Exception("The value could not be found")

    def __delitem__(self, key):
        hash = self.get_hash(key)
        start_pos = hash

        while self.arr[hash] is not None:
            if self.arr[hash][0] == key:
                self.arr[hash] = None
                return

            hash = (hash + 1) % self.MAX

            if hash == start_pos:
                raise Exception("Couldn't find the element to delete")

        raise KeyError(f"Key {key} not found")


if __name__ == "__main__":
    t = HashTable()
    t["march 62552123"] = "abc"
    t["march 6255"] = "easy as"
    print(t["march 6255"])
    print(t.arr)
    # print(t["march 6255"])
    del t["march 6255"]
    print(t.arr)
