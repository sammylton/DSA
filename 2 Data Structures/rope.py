import random
from collections import namedtuple

Answer = namedtuple('Answer', 'res')

class RopeNode:
    __slots__ = ('val','left','right','parent','priority','size')
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.priority = random.random()
        self.size = 1

def get_size(v): return v.size if v else 0
def update(v):
    if not v: return
    v.size = 1 + get_size(v.left) + get_size(v.right)
    if v.left:  v.left.parent=v
    if v.right: v.right.parent=v

def split(v, k):
    if not v: return None, None
    if get_size(v.left) >= k:
        l, r = split(v.left, k)
        v.left = r; update(v); return l, v
    else:
        l, r = split(v.right, k - get_size(v.left) - 1)
        v.right = l; update(v); return v, r

def merge(l, r):
    if not l: return r
    if not r: return l
    if l.priority > r.priority:
        l.right = merge(l.right, r); update(l); return l
    else:
        r.left = merge(l, r.left); update(r); return r

def process_rope(s, qs):
    root = None
    for c in s: root = merge(root, RopeNode(c))
    for i,j,k in qs:
        l, r = split(root, i)
        mid, r2 = split(r, j - i + 1)
        root = merge(l, r2)
        l2, r3 = split(root, k)
        root = merge(merge(l2, mid), r3)
    return root

def build_string(v):
    if not v: return ""
    return build_string(v.left) + v.val + build_string(v.right)

def main():
    s = input().strip()
    q = int(input())
    qs = [tuple(map(int, input().split())) for _ in range(q)]
    root = process_rope(s, qs)
    print(build_string(root))

if __name__ == "__main__":
    main()
