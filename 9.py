A.
# WAP to read a file and print the total number of characters, words, and lines

filename=input("Enter filename:")
file=open(filename, 'r') 
lines = file.readlines()
num_lines = len(lines)
num_words = sum(len(line.split()) for line in lines)
num_chars = sum(len(line) for line in lines)
print(num_chars, num_words, num_lines)

B.
# WAP to calculate the frequency of each character in a file

def character_frequency_in_file(filename):
    freq = {}
    with open(filename, 'r') as file:
        text = file.read()
        for char in text:
            freq[char] = freq.get(char, 0) + 1
    print(freq)

character_frequency_in_file("sample.txt")

C.
# WAP to print the words in a file in reverse order

def reverse_words_in_file(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    print(' '.join(reversed(words)))

reverse_words_in_file("sample.txt")
