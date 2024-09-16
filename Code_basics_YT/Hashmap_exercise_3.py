word_dict = {}

with open("poem.txt", "r") as f:
    for lines in f:
        words = lines.split()  # Strip leading/trailing whitespace or newline characters
        for word in words:
            word = word.strip()  # Clean punctuation and convert to lowercase
            print(word)
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
word_dict
