stock_prices_list = []
stock_prices_dict = {}


def print_stock_price_list():
    with open("stock_prices.csv", "r") as f:
        for line in f:
            token = line.split(",")
            date = token[0]
            price = token[1]
            stock_prices_list.append([date, price])
    return stock_prices_list


def print_stock_price_dict():
    with open("stock_prices.csv", "r") as f:
        for line in f:
            token = line.split(",")
            date = token[0]
            price = token[1]
            stock_prices_dict[date] = price
    return stock_prices_dict


class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        # Simple implementation of Hashmap
        # However does not fix issue of collision
        # hash = self.get_hash(key)
        # self.arr[hash] = value

        found = False
        hash = self.get_hash(key)
        for index, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[hash].append((key, value))

    def __getitem__(self, key):
        # Simple implementation of Hashmap
        # However does not fix issue of collision
        # hash = self.get_hash(key)
        # return self.arr[hash]

        hash = self.get_hash(key)
        for element in self.arr[hash]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        # Simple implementation of Hashmap
        # However does not fix issue of collision
        # hash = self.get_hash(key)
        # self.arr[hash] = None
        hash = self.get_hash(key)
        for index, kv in enumerate(self.arr[hash]):
            if kv[0] == key:
                del [self.arr[hash][index]]


if __name__ == "__main__":
    price_list = print_stock_price_list()
    price_dict = print_stock_price_dict()

    print(price_dict["march 6"])

    t = HashTable()
    t["march 62552123"] = "abc"
    t["march 6255"] = "easy as"
    print(t.get_hash("march 62552123"))
    print(t.get_hash("march 6255"))
    # print(t["march 6"])
    print(t.arr)
    print(t["march 6255"])
    del t["march 6255"]
    print(t.arr)
