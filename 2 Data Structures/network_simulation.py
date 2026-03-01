import sys
from collections import deque

def process_packets(size, packets):
    finish_times = deque()
    result = []

    for arrival, duration in packets:
        while finish_times and finish_times[0] <= arrival:
            finish_times.popleft()

        if len(finish_times) == size:
            result.append(-1)
        else:
            start = arrival if not finish_times else finish_times[-1]
            finish_times.append(start + duration)
            result.append(start)

    return result

if __name__ == "__main__":
    s, n = map(int, sys.stdin.readline().split())
    packets = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    for r in process_packets(s, packets):
        print(r)
