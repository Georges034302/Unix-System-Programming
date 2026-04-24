#!/usr/bin/env python3

def vowel_count(segment):
    count = 0

    for char in segment:
        if char in "aeiou":
            count += 1

    return count

def match_word(word):
    for segment in word.split("z"):
        if vowel_count(segment) == 2:
            return True

    return False

def word_count(sentence):
    count = 0

    for word in sentence.split():
        if match_word(word):
            count += 1

    return count

def main():
    sentence = input("sentence: ")

    while sentence != "*":
        print(f"Matching words: {word_count(sentence.lower())}")
        sentence = input("sentence: ")

if __name__ == "__main__":
    main()
