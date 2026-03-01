# python3
import sys

def main():
    n = int(sys.stdin.readline())
    book = {}
    out = []

    for _ in range(n):
        cmd = sys.stdin.readline().split()
        if cmd[0] == "add":
            book[cmd[1]] = cmd[2]
        elif cmd[0] == "del":
            book.pop(cmd[1], None)
        else:
            out.append(book.get(cmd[1], "not found"))

    print("\n".join(out))

if __name__ == "__main__":
    main()
