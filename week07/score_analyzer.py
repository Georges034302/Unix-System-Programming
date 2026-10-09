#!/usr/bin/env python3
"""
Analyze entered scores, counting passes and failures and tracking statistics.

Usage:
    python3 score_analyzer.py
    Enter scores one at a time; enter -1 to finish.
"""

count = total = passes = fails = 0
min_score = max_score = None  # None until the first score is entered

score = int(input("Score (-1 to stop): "))  # Read the first score or the stop value.

while score != -1:
    count += 1  # Count this score.
    total += score  # Add it to the running total.

    if min_score is None or score < min_score: min_score = score  # Update the lowest score.
    if max_score is None or score > max_score: max_score = score  # Update the highest score.

    if score >= 50: passes += 1  # Scores of 50 or more are passes.
    else:           fails  += 1  # Lower scores are failures.

    score = int(input("Score (-1 to stop): "))  # Read the next score or stop value.

# --- Summary ---
print(f"\nCount   : {count}")
print(f"Total   : {total}")
print(f"Average : {total / count:.2f}" if count > 0 else "Average : [no data]")  # Avoid dividing by zero when no scores were entered.
print(f"Min     : {min_score if min_score is not None else '[no data]'}")
print(f"Max     : {max_score if max_score is not None else '[no data]'}")
print(f"Passes  : {passes}")
print(f"Fails   : {fails}")
