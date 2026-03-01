# python3
import sys

p = 10**9 + 7
x = 263

def poly_hash(s, m):
    h = 0
    for c in reversed(s):
        h = (h * x + ord(c)) % p
    return h % m

def main():
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    table = [[] for _ in range(m)]
    out = []

    for _ in range(n):
        cmd = sys.stdin.readline().split()
        if cmd[0] == "add":
            h = poly_hash(cmd[1], m)
            if cmd[1] not in table[h]:
                table[h].insert(0, cmd[1])
        elif cmd[0] == "del":
            h = poly_hash(cmd[1], m)
            if cmd[1] in table[h]:
                table[h].remove(cmd[1])
        elif cmd[0] == "find":
            h = poly_hash(cmd[1], m)
            out.append("yes" if cmd[1] in table[h] else "no")
        else:
            idx = int(cmd[1])
            out.append(" ".join(table[idx]))

    print("\n".join(out))

if __name__ == "__main__":
    main()
