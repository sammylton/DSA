class DSU:
    def __init__(self, sizes):
        self.parent = list(range(len(sizes)))
        self.rank = [0] * len(sizes)
        self.size = sizes
        self.max_size = max(sizes)

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, dest, src):
        dest = self.find(dest)
        src = self.find(src)
        if dest == src:
            return self.max_size

        if self.rank[dest] < self.rank[src]:
            dest, src = src, dest

        self.parent[src] = dest
        self.size[dest] += self.size[src]
        self.size[src] = 0

        if self.rank[dest] == self.rank[src]:
            self.rank[dest] += 1

        self.max_size = max(self.max_size, self.size[dest])
        return self.max_size


if __name__ == "__main__":
    n, m = map(int, input().split())
    sizes = list(map(int, input().split()))
    dsu = DSU(sizes)

    # for _ in range(m):
    #     d, s = map(int, input().split())
    #     print(dsu.union(d - 1, s - 1))
    results = []
    for _ in range(m):
        d, s = map(int, input().split())
        results.append(str(dsu.union(d - 1, s - 1)))

    print("\n".join(results))
