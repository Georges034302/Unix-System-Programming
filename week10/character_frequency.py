#!/usr/bin/env python3
"""
Count a selected character's frequency in each sentence.
Usage:
    python3 character_frequency.py
    Enter a sentence and character for each result.
    Type . at the sentence prompt to finish.
"""

# Count occurrences of the selected character in the sentence.
def char_frequency(sentence, character):
    return sentence.count(character)

# Return the results dictionary with one additional character frequency.
def add_result(results, character, frequency):
    updated_results = results.copy()
    entry_number = len(updated_results) + 1
    updated_results[entry_number] = (character, frequency)
    return updated_results

# Display each character and its stored frequency.
def show_results(results):
    for character, frequency in results.values():
        print(f"{character} --> {frequency}")

# Read sentences until the sentinel and call the frequency, mapping, and display functions.
def main():
    results = {}

    while True:
        sentence = input("Enter a sentence (. to finish): ").strip()
        if sentence == ".":
            break

        character = input("Enter a character: ")
        frequency = char_frequency(sentence, character)
        results = add_result(results, character, frequency)

    show_results(results)

if __name__ == "__main__":
    main()
