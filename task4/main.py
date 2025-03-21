a = list(map(int, open("tetst1.txt").read().split()))
a.sort()
n = len(a)
m = a[n//2] if n % 2 else a[n//2 - 1]
print(sum(abs(x - m) for x in a))
