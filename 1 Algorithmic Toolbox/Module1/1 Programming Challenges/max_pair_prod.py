def max_pair_prod(l: list) -> tuple:
    j = 0
    k = 0
    for i in range(1,len):
        if l[i] > l[j]:
            j = i
    for i in range(1,len):
        if l[i] > l[k] and i != j:
            k = i
    return l[j]*l[k]

if __name__ == '__main__':
    len = int(input())
    l = list(map(int, input().split()))
    print(max_pair_prod(l))