#!/usr/bin/env python3

count = total = passes = fails = 0
min_score = max_score = None  # None until the first score is entered

score = int(input("Score (-1 to stop): "))

while score != -1:
    count += 1
    total += score

    if min_score is None or score < min_score: min_score = score  # track lowest
    if max_score is None or score > max_score: max_score = score  # track highest

    if score >= 50: passes += 1  # 50 and above is a pass
    else:           fails  += 1

    score = int(input("Score (-1 to stop): "))

# --- Summary ---
print(f"\nCount   : {count}")
print(f"Total   : {total}")
print(f"Average : {total / count:.2f}" if count > 0 else "Average : [no data]")
print(f"Min     : {min_score if min_score is not None else '[no data]'}")
print(f"Max     : {max_score if max_score is not None else '[no data]'}")
print(f"Passes  : {passes}")
print(f"Fails   : {fails}")
