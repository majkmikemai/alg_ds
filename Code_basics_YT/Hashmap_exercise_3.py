# class HashTable:
#     def __init__(self) -> None:
#         self.MAX = 100
#         self.arr = [[] for i in range(self.MAX)]

#     def get_hash(self, key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.MAX

#     def __setitem__(self, key, value):
#         # Simple implementation of Hashmap
#         # However does not fix issue of collision
#         # hash = self.get_hash(key)
#         # self.arr[hash] = value

#         found = False
#         hash = self.get_hash(key)
#         for index, element in enumerate(self.arr[hash]):
#             if len(element) == 2 and element[0] == key:
#                 self.arr[hash][index] = (key, value)
#                 found = True
#                 break
#         if not found:
#             self.arr[hash].append((key, value))

#     def __getitem__(self, key):
#         # Simple implementation of Hashmap
#         # However does not fix issue of collision
#         # hash = self.get_hash(key)
#         # return self.arr[hash]

#         hash = self.get_hash(key)
#         for element in self.arr[hash]:
#             if element[0] == key:
#                 return element[1]

#     def __delitem__(self, key):
#         # Simple implementation of Hashmap
#         # However does not fix issue of collision
#         # hash = self.get_hash(key)
#         # self.arr[hash] = None
#         hash = self.get_hash(key)
#         for index, kv in enumerate(self.arr[hash]):
#             if kv[0] == key:
#                 del [self.arr[hash][index]]


word_dict = {}

with open("poem.txt", "r") as f:
    for lines in f:
        words = lines.split()
        for word in words:
            word = word.strip()
            print(word)
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
word_dict

word_dict = {}

with open("poem.txt", "r") as f:
    for line in f:  # Strip leading/trailing whitespace or newline characters
        words = line.split()  # Split by whitespace to get individual words
        for word in words:
            line = word.strip()  # Clean punctuation and convert to lowercase
            if word in word_dict:
                word_dict[word] += 1  # Increment the count if word already exists
            else:
                word_dict[word] = 1  # Add the word with count 1 if it doesn't exist

# Print the word dictionary
print(word_dict)


# if __name__ == "__main__":
#     price_list = print_stock_price_list()
#     price_dict = print_stock_price_dict()

#     print(price_dict["march 6"])

#     t = HashTable()
