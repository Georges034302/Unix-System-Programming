#!/usr/bin/env python3
"""
Find words with exactly two vowels between 'z' delimiters.
Usage: python3 two_vowels_matcher.py
Reads sentences and counts words matching the pattern (enter '*' to exit).
"""

# Counts vowels (a, e, i, o, u) in a text segment.
def vowel_count(segment):
    return sum(1 for char in segment if char in "aeiou")

# Returns True if word has exactly 2 vowels in any z-delimited segment.
def match_word(word):
    for segment in word.split("z"):
        if vowel_count(segment) == 2:
            return True
    return False

# Counts matching words in a sentence.
def word_count(sentence):
    return sum(1 for word in sentence.split() if match_word(word))

# Prompts user for sentences, counts matching words until '*' entered.
def main():
    sentence = input("sentence: ")
    while sentence != "*":
        print(f"Matching words: {word_count(sentence.lower())}")
        sentence = input("sentence: ")

if __name__ == "__main__":
    main()
