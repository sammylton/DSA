# python3
import sys
import random

def read_input():
    s = sys.stdin.readline().strip()
    q = int(sys.stdin.readline())
    queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(q)]
    return s, queries

def precompute_hashes(s, p, mod):
    n = len(s)
    h = [0] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (h[i - 1] * p + ord(s[i - 1])) % mod
    return h

def precompute_powers(p, n, mod):
    pw = [1] * (n + 1)
    for i in range(1, n + 1):
        pw[i] = (pw[i - 1] * p) % mod
    return pw

def get_sub_hash(h, pw, l, r, mod):
    return (h[r] - pw[r - l] * h[l]) % mod

def main():
    s, queries = read_input()
    mod1, mod2 = 10**9 + 7, 10**9 + 9
    p = random.randint(256, 1000)

    h1 = precompute_hashes(s, p, mod1)
    h2 = precompute_hashes(s, p, mod2)
    pw1 = precompute_powers(p, len(s), mod1)
    pw2 = precompute_powers(p, len(s), mod2)

    out = []
    for a, b, l in queries:
        if (get_sub_hash(h1, pw1, a, a+l, mod1) ==
            get_sub_hash(h1, pw1, b, b+l, mod1) and
            get_sub_hash(h2, pw2, a, a+l, mod2) ==
            get_sub_hash(h2, pw2, b, b+l, mod2)):
            out.append("Yes")
        else:
            out.append("No")
    print("\n".join(out))

if __name__ == "__main__":
    main()
