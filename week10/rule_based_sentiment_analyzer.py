#!/usr/bin/env python3
import sys

POSITIVE_WORDS = {"good", "great", "excellent", "happy", "love", "nice", "amazing", "fast", "clean", "safe"}
NEGATIVE_WORDS = {"bad", "terrible", "awful", "sad", "hate", "slow", "dirty", "broken", "unsafe", "angry"}

def normalize_word(word):
    return "".join(char.lower() for char in word if char.isalpha())

def score_sentence(sentence):
    positive = 0
    negative = 0

    for raw_word in sentence.split():
        word = normalize_word(raw_word)

        if word in POSITIVE_WORDS:
            positive += 1
        elif word in NEGATIVE_WORDS:
            negative += 1

    return positive, negative

def classify_sentence(sentence):
    positive, negative = score_sentence(sentence)

    if positive > negative:
        return "positive", positive, negative

    if negative > positive:
        return "negative", positive, negative

    return "neutral", positive, negative

def main():
    for line in sys.stdin:
        sentence = line.rstrip("\n")
        label, positive, negative = classify_sentence(sentence)
        print(f"{label.upper():8s} | +{positive} -{negative} | {sentence}")

if __name__ == "__main__":
    main()
