# NOTE: Graded 100/100
# NOTE: All tests pass

import sys
import re

html = sys.stdin.read()
spec = dict()

re_tr = re.compile(r"<tr[^>]*>(.*?)</tr>", re.I | re.DOTALL)
re_td = re.compile(r"<td[^>]*>(.*?)</td>", re.I | re.DOTALL)
re_pn = re.compile(r"<a[^>]*>\s*(\w+)\s+(\w+)\s*</a>", re.I | re.DOTALL)
re_sn = re.compile(r"(\w[^&]+)&nbsp", re.I | re.DOTALL)

for r in filter(bool, map(re_td.findall, re_tr.findall(html))):
    name = re_pn.findall(r[0])[0]
    num = re_sn.findall(r[7])[0]

    fac = r[10]
    if not fac in spec:
        spec[fac] = []

    spec[fac].append((
        num[0], f"{name[0].upper()} {name[1].title()}",
        fac, int(num[1:])
    ))

def order_stud_num(stud):
    n = stud[3]
    return (n % 2 == 0, n)

for spec_code in sorted(spec.keys()):
    students = spec[spec_code]
    print(f"{spec_code}:")
    for pos, stud in enumerate(sorted(students, key=order_stud_num), 1):
        print(f"{pos:2}: {stud[0]} {stud[1]:<18} {stud[2]:<3} {stud[3]}")
    print()