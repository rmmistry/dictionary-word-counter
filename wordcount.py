# put your code here.
def formatting(word_count_dict):
    for word in word_count_dict.items():
        print "{} {}".format(word[0], word[1])

def word_count(file_name):
    words = {}

    text_file = open(file_name)

    for line in text_file:
        strip_line = line.rstrip()
        split_line = strip_line.split()

        for word in split_line:
            count = words.get(word, 0) + 1
            words[word] = count

    return formatting(words)

word_count("test.txt")
