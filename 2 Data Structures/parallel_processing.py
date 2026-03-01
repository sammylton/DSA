import heapq

if __name__ == "__main__":
    n, m = map(int, input().split())
    jobs = list(map(int, input().split()))

    heap = [(0, i) for i in range(n)]  # (finish_time, thread_id)
    heapq.heapify(heap)

    for job in jobs:
        time, tid = heapq.heappop(heap)
        print(tid, time)
        heapq.heappush(heap, (time + job, tid))
