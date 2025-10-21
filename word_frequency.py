#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re
import string
#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    sentence = input("Enter a sentence: ")
    while (is_sentence(sentence) == False):
        print("Invalid sentence. Please try again")
        sentence = string(input("Enter a sentence: "))
    clean_user_sentence = sentence.lower()
    split_input = clean_user_sentence.translate(str.maketrans('', '', string.punctuation)).split()
    return split_input

def calculate_frequencies(sentence):
    word_count = []
    index = 0
    words = []
    for i in sentence:
        if i in words:
            index = words.index(i)
            word_count[index]+=1
        else:
            words.append(i)
            word_count.append(1)
    return words, word_count
    

def print_frequencies(words, frequencies):
    increment = 0
    for j in words:
        print(j+": "+str(frequencies[increment]))
        increment+=1

def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)

main()
