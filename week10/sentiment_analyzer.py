#!/usr/bin/env python3
"""
Analyze sentiment of text using positive/negative word lists.
Usage: python3 rule_based_sentiment_analyzer.py
Prompts for text input, analyzes sentiment, and repeats until 'x' is entered.
"""
POSITIVE_WORDS = {"good", "great", "excellent", "happy", "love", "nice", "amazing", "fast", "clean", "safe", "beautiful", "wonderful", "fantastic", "awesome", "enjoy", "like", "brilliant", "perfect", "brilliant", "smart", "kind"}
NEGATIVE_WORDS = {"bad", "terrible", "awful", "sad", "hate", "slow", "dirty", "broken", "unsafe", "angry", "ugly", "horrible", "pathetic", "stupid", "dumb", "mean", "rude", "annoying", "disgusting", "waste"}
NEGATION_WORDS = {"not", "no", "never", "dont", "doesnt", "didnt", "isnt", "wasnt", "cant", "wont"}

# Removes non-alphabetic characters and converts word to lowercase.
def normalize_word(word):
    return "".join(char.lower() for char in word if char.isalpha())

# Counts positive and negative words in a sentence.
def score_sentence(sentence):
    positive = 0
    negative = 0
    words = sentence.split()
    for index, raw_word in enumerate(words):
        word = normalize_word(raw_word)
        previous_words = words[max(0, index - 2):index]
        is_negated = any(
            normalize_word(previous_word) in NEGATION_WORDS
            for previous_word in previous_words
        )

        if word in POSITIVE_WORDS:
            if is_negated:
                negative += 1
            else:
                positive += 1
        elif word in NEGATIVE_WORDS:
            if is_negated:
                positive += 1
            else:
                negative += 1
    return positive, negative

# Classifies sentence as positive, negative, or neutral based on word scores.
def classify_sentence(sentence):
    positive, negative = score_sentence(sentence)
    if positive > negative:
        return "positive", positive, negative
    if negative > positive:
        return "negative", positive, negative
    return "neutral", positive, negative

# Prompts user for text, analyzes sentiment, repeats until 'x' entered.
def main():
    print("Enter text to analyze sentiment (enter 'x' to exit):\n")
    while True:
        sentence = input(">>> ").strip()
        if sentence.lower() == "x":
            print("Goodbye!")
            break
        if sentence == "":
            continue
        label, positive, negative = classify_sentence(sentence)
        print(f"{label.upper():8s} | +{positive} -{negative} | {sentence}\n")

if __name__ == "__main__":
    main()
