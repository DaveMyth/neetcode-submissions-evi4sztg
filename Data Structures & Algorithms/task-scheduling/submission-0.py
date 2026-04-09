class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        taskFreq = {}

        for task in tasks:
            taskFreq[task] = taskFreq.get(task,0)-1

        minHeap = list(taskFreq.values())
        heapq.heapify(minHeap)

        q = deque()
        time = 0

        while minHeap or q:
            time += 1
            if minHeap:
                task = heapq.heappop(minHeap)
                task += 1

                if task < 0:
                    q.append([task, time + n])

            if q and q[0][1] <= time:
                heapq.heappush(minHeap, q.popleft()[0])

        return time