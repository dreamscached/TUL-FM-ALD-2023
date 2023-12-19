# NOTE: Graded 100/100
# NOTE: All test pass

import sys

for line in sys.stdin:
    s = line.lower().strip()
    pal = s == s[::-1]
    print("ano" if pal else "ne")
