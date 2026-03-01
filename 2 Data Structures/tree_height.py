import sys
from collections import deque

def compute_height(n, parents):
    children = [[] for _ in range(n)]
    root = -1

    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            children[parents[i]].append(i)

    height = 0
    q = deque([root])

    while q:
        height += 1
        for _ in range(len(q)):
            node = q.popleft()
            for c in children[node]:
                q.append(c)

    return height

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    parents = list(map(int, sys.stdin.readline().split()))
    print(compute_height(n, parents))
