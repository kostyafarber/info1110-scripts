import sys

if len(sys.argv) < 3:
    print("Cannot process")
    sys.exit()

original_word = str(sys.argv[2])
word = original_word.lower()

word_count = 0

file = open(sys.argv[1], "r")
lines = file.read().lower().split()

for s in lines:
    if s == word:
        word_count += 1

if word_count > 0:
    print('"{0}" has been found {1} times'.format(original_word, word_count))

else:
    print('"{0}" does not exist in this file'.format(original_word))
