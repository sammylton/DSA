# Car Fueling problem
# Input: A car which can travel at most L kilometers with full tank, a source point A, 
# a destination point B and n gas stations at distances x1 <= x2 <= *** <= xn in kilometers 
# from A along the path from A to B.
# 
# Output: The minimum number of refills to get from A to B, besides refill at A.


from typing import List


def minRefills(x: List[float], n: int, L: float) -> int:
    """
    Args:
    x (list): list of gas station distances including start and end points
    n (int): number of gas stations
    L (int): driving range (on a full tank)
    Returns:
    int: number of gas station stops/refills
    """
    numRefills = 0
    currStop = 0
    lastStop = 0
    # print("C", "L", "N") # check
    while currStop < n+1:
        currStop += 1
        if x[currStop] - x[lastStop] > L:
            numRefills += 1
            lastStop = currStop - 1
        # print(currStop, lastStop, numRefills) # check
    return numRefills

if __name__ == "__main__":
    arr = [0, 200, 400, 600, 800]
    print(minRefills(arr, len(arr)-2, 400))