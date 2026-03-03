def minRefills(x, n, L):
    """
    x (array): array of gas station distances including start and end points
    n (int): number of gas stations
    L (int): driving range (on a full tank)
    """
    numRefills = 0
    currStop = 0
    lastStop = 0
    print("C", "L", "N")
    while currStop < n+1:
        currStop += 1
        if x[currStop] - x[lastStop] > L:
            numRefills += 1
            lastStop = currStop - 1
        print(currStop, lastStop, numRefills)
    return numRefills

if __name__ == "__main__":
    arr = [0, 200, 400, 600, 800]
    print(minRefills(arr, len(arr)-2, 400))