# put your code here.

words = {}

def word_counter(file_name):
    text_file = open(file_name)

    for line in text_file:
        strip_line = line.rstrip()
        split_line = strip_line.split()

        for word in split_line:
            count = words.get(word, 0) + 1
            words[word] = count

        for item in words.items():
            return item

word_counts = word_counter("test.txt")

print word_counts
