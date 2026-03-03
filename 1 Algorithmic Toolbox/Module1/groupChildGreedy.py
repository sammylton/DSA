# Grouping childer problem
# 
# Many children came to a celebration.
# Organize them into the minimum possible number of groups such that the age of any two
# children in the same group differ by at most one year.


from typing import List


def minGroups(x: List[float], count: int = 0) -> int:
    """
    Args:
    x (list): List of children ages in ASCENDING order
    count (int): number of groups already counted
    Return:
    int: number of groups to be created
    """
    no = len(x)
    i = 0
    while i < no:
        right = x[i] + 1
        # left = x[i]
        # print(i, left, right)
        while right > x[i]:
            i += 1
            if i == no:
                break
        count += 1
        # print(i, count)
    return count
    
if __name__ == "__main__":
    x = [0.9, 1.2, 1.3, 2.1, 2.5, 5.2]
    print(minGroups(x))