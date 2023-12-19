# NOTE: Graded 75/100
# WARN: 4th test DOES NOT PASS!

import itertools
import sys

def get_next_pal(n):
    for n in itertools.count(n+1):
        s = str(n)
        if s == s[::-1]:
            return n

for line in sys.stdin:
    n = int(line)
    if n == -1:
          break

    print(get_next_pal(n))