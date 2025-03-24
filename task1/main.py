import sys

def s(n, p):
    r, c = [], 1
    while True:
        it = []
        t = c
        for _ in range(p):
            it.append(t)
            t += 1
            if t > n:
                t -= n
        r.append(it[0])
        c = it[-1]
        if c == 1:
            break
    return r

n, p = map(int, sys.argv[1:3])
print("".join(map(str, s(n, p))))
