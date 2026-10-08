#!/usr/bin/env python3
"""
Play a short multiple-choice quiz.
Usage:
    python3 quiz_game.py
    Answer each question with a, b, or c.
"""

# Display one question and its answer choices.
def show_question(question, choices):
    print(question)
    for choice in choices:
        print(choice)


# Check whether the selected answer matches the correct answer.
def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer


# Ask all questions and return the number answered correctly.
def run_quiz(questions):
    score = 0
    for question, choices, correct_answer in questions:
        show_question(question, choices)
        answer = input("Your answer: ")
        if check_answer(answer, correct_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The answer is {correct_answer}.\n")
    return score


# Display the final quiz score.
def show_result(score, total):
    print(f"Your score: {score}/{total}")


# Return the quiz questions, choices, and correct answers.
def load_questions():
    return [
        (
            "Which function displays text in Python?",
            ["a) input", "b) print", "c) len"],
            "b",
        ),
        (
            "Which type represents True or False?",
            ["a) bool", "b) str", "c) list"],
            "a",
        ),
        (
            "Which keyword starts a function definition?",
            ["a) for", "b) class", "c) def"],
            "c",
        ),
    ]


# Set up the questions, run the quiz, and show the result.
def main():
    questions = load_questions()
    score = run_quiz(questions)
    show_result(score, len(questions))

if __name__ == "__main__":
    main()
