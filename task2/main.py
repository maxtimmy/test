import sys

if len(sys.argv) < 3:
    print("Usage: python main.py <file1> <file2>")
    sys.exit(1)

f_path = sys.argv[1]
g_path = sys.argv[2]

with open(f_path) as f:
    x, y = map(float, f.readline().split())
    r = float(f.readline())

with open(g_path) as g:
    for line in g:
        a, b = map(float, line.split())
        d = ((a - x) ** 2 + (b - y) ** 2) ** 0.5
        if abs(d - r) < 1e-9:
            print(0)
        elif d < r:
            print(1)
        else:
            print(2)
