import sys
import re

def to_chart(s):
    s = re.sub(r"\s", "", s)
    s = s.strip().lower()
    chart = [0 for _ in range(ord('a'), ord('z') + 1)]

    for c in map(ord, s):
        chart[ord('a') - c] += 1

    return tuple(chart)

CMP_EXACT = 0
CMP_NEAR = 1
CMP_DIFF = 2

def cmp_chart(a, b):
    if a == b:
        return CMP_EXACT

    diff = list(map(lambda x, y: abs(x - y), a, b))
    count_diff = len(list(filter(lambda x: x > 0, diff)))
    max_diff = max(diff)

    if count_diff > 1 or max_diff > 1:
        return CMP_DIFF

    return CMP_NEAR

while True:
    word = sys.stdin.readline()
    test = sys.stdin.readline()

    if not word or not test:
        break

    wc = to_chart(word)
    tc = to_chart(test)
    ret = cmp_chart(wc, tc)

    if ret == CMP_EXACT:
        print("ANAGRAMS")
    elif ret == CMP_NEAR:
        print("NEAR ANAGRAMS")
    else:
        print("NOT ANAGRAMS")