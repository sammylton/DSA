from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    result = []

    for i, num in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] <= num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())
    print(*max_sliding_window(nums, k))
