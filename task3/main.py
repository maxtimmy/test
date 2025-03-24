import json
import sys

if len(sys.argv) != 4:
    print("python main.py <tests_file> <values_file> <report_file>")
    sys.exit(1)

p1 = sys.argv[1]
p2 = sys.argv[2]
p3 = sys.argv[3]

def f(o, d):
    if 'id' in o and o['id'] in d:
        o['value'] = d[o['id']]
    if 'values' in o:
        for v in o['values']:
            f(v, d)

with open(p1) as fi:
    ts = json.load(fi)
with open(p2) as fi:
    vs = json.load(fi)
d = {x['id']: x['value'] for x in vs['values']}
for t in ts['tests']:
    f(t, d)
with open(p3, "w") as fo:
    json.dump(ts, fo, indent=2)
