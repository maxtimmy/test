import json
def f(o, d):
    if 'id' in o and o['id'] in d:
        o['value'] = d[o['id']]
    if 'values' in o:
        for v in o['values']:
            f(v, d)
p1 = "tests.json"
p2 = "values.json"
p3 = "report.json"
with open(p1) as fi:
    ts = json.load(fi)
with open(p2) as fi:
    vs = json.load(fi)
d = {x['id']: x['value'] for x in vs['values']}
for t in ts['tests']:
    f(t, d)
with open(p3, "w") as fo:
    json.dump(ts, fo, indent=2)
