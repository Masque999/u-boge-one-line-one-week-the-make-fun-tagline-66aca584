import os

LINE = "Describe it once, and an AI agent builds it while you watch \u2014 the best one takes the prize."

# The entry must be exactly one line of 1-100 characters, with no
# leading or trailing whitespace and a proper ending.
assert 1 <= len(LINE) <= 100, f"line is {len(LINE)} chars"
assert "\n" not in LINE
assert LINE == LINE.strip(), "line has leading or trailing whitespace"
assert LINE[-1] in ".!?", "line must end with terminal punctuation"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
