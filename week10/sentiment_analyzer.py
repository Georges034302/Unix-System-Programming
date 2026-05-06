#!/usr/bin/env python3
"""
Analyze sentiment of text using positive/negative word lists.
Usage: python3 sentiment_analyzer.py
Reads sentences, analyzes sentiment, and repeats until 'x' is entered.
"""

POSITIVE_WORDS = {"good", "great", "excellent", "happy", "love", "nice", "amazing", "fast", "clean", "safe", "beautiful", "wonderful", "fantastic", "awesome", "enjoy", "like", "brilliant", "perfect", "smart", "kind"}
NEGATIVE_WORDS = {"bad", "terrible", "awful", "sad", "hate", "slow", "dirty", "broken", "unsafe", "angry", "ugly", "horrible", "pathetic", "stupid", "dumb", "mean", "rude", "annoying", "disgusting", "waste"}

# Removes non-alphabetic characters and converts word to lowercase.
def normalize_word(word):
    return "".join(char.lower() for char in word if char.isalpha())

# Returns True if word is a negation marker (not, do, does, don't, didn't, won't, etc).
def is_negation_word(word):
    return word in {"not", "do", "does"} or word.endswith("nt")

# Returns True if the word at index is preceded by a negation.
def is_negated(words, index):
    window = words[max(0, index - 2):index]
    return any(is_negation_word(normalize_word(word)) for word in window)

# Counts positive and negative words in a sentence, handling negations.
def score_sentence(sentence):
    positive = 0
    negative = 0
    words = sentence.split()
    
    for i, raw_word in enumerate(words):
        word = normalize_word(raw_word)
        
        if is_negation_word(word):
            continue
        
        negated = is_negated(words, i)
        
        if word in POSITIVE_WORDS:
            if negated:
                negative += 1
            else:
                positive += 1
        elif word in NEGATIVE_WORDS:
            if negated:
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
        if sentence == "x":
            break
        if sentence:
            label, positive, negative = classify_sentence(sentence)
            print(f"{label.upper():8s} | +{positive} -{negative} | {sentence}\n")
    print("Goodbye!")

if __name__ == "__main__":
    main()
