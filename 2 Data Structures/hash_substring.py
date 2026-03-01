# python3
import sys

def main():
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()

    p = 263
    mod = 10**9 + 7
    n, m = len(text), len(pattern)

    if m > n:
        return

    def poly_hash(s):
        h = 0
        for c in reversed(s):
            h = (h * p + ord(c)) % mod
        return h

    p_hash = poly_hash(pattern)
    hashes = [0] * (n - m + 1)
    hashes[-1] = poly_hash(text[n - m:])

    power = pow(p, m, mod)
    for i in range(n - m - 1, -1, -1):
        hashes[i] = (p * hashes[i + 1] + ord(text[i]) -
                     power * ord(text[i + m])) % mod

    res = []
    for i in range(n - m + 1):
        if hashes[i] == p_hash and text[i:i+m] == pattern:
            res.append(str(i))

    print(" ".join(res))

if __name__ == "__main__":
    main()
