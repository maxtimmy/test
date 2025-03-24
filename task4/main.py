import sys

if len(sys.argv) != 2:
    print("python main.py <filename>")
    sys.exit(1)

with open(sys.argv[1]) as f:
    a = list(map(int, f.read().split()))
a.sort()
n = len(a)
m = a[n // 2] if n % 2 else a[n // 2 - 1]
print(sum(abs(x - m) for x in a))
