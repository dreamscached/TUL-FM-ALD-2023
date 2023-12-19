# NOTE: Graded 100/100
# NOTE: All tests pass

from collections import OrderedDict
import sys
import re

text = sys.stdin.read().strip()
words = text.replace("\n", " ").lower()
words = re.sub(r"(\s){2,}", r"\1", words)
words = words.split()
phrases = list()

for idx in range(1, len(words)):
    phrase = " ".join(words[idx-1:idx+1])
    phrases.append(phrase)

w_count = OrderedDict()
for word in words:
    w_count[word] = w_count.get(word, 0) + 1

p_count = OrderedDict()
for phrase in phrases:
    p_count[phrase] = p_count.get(phrase, 0) + 1

def print_table(title, rows, long=False):
    fmt_str = f" - %-{20 if long else 12}s %.2f%% (%d)"
    print(title)

    for row in rows:
        what, perc, n = row
        print(fmt_str % (what, perc, n))

def sort_by_count(data):
    return sorted(data.items(),
        key=lambda it: it[1],
        reverse=True)

def to_rows(data, total, top=15):
    rows = sort_by_count(data)
    for idx in range(len(rows)):
        what, n = rows[idx]
        rows[idx] = (what, n / total * 100, n)

    return rows[:top]

print_table("Word Frequency:",
    to_rows(w_count, len(words)), long=False)

print_table("Phrase Frequency:",
    to_rows(p_count, len(words)), long=True)

