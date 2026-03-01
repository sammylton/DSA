def sift_down(i, a, swaps):
    n = len(a)
    min_i = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and a[l] < a[min_i]:
        min_i = l
    if r < n and a[r] < a[min_i]:
        min_i = r

    if i != min_i:
        swaps.append((i, min_i))
        a[i], a[min_i] = a[min_i], a[i]
        sift_down(min_i, a, swaps)


def build_heap(a):
    swaps = []
    for i in range(len(a)//2 - 1, -1, -1):
        sift_down(i, a, swaps)
    return swaps


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    swaps = build_heap(a)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
