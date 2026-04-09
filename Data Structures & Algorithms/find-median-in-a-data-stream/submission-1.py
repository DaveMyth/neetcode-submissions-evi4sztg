class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            heapq.heappush(self.maxHeap, -1*num)
            return

        if num <= -1*self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -1*num)
        else:
            heapq.heappush(self.minHeap, num)

        if len(self.minHeap) > len(self.maxHeap)+1:
            heapq.heappush(self.maxHeap, -1*heapq.heappop(self.minHeap))

        elif len(self.maxHeap) > len(self.minHeap)+1:
            heapq.heappush(self.minHeap, -1*heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0] 
        elif len(self.minHeap) < len(self.maxHeap):
            return self.maxHeap[0] * -1
        else:
            return (self.minHeap[0] + -1*self.maxHeap[0])/2