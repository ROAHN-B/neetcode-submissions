class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for ele in stones:
            max_heap.append(-ele)

        while len(max_heap) > 1:
            heapq.heapify(max_heap)
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x > y:
                res = x - y
                heapq.heappush(max_heap, -res)
            elif y > x:
                res = y - x
                heapq.heappush(max_heap, -res)
            else:
                res = y - x
                heapq.heappush(max_heap, -res)
        return (-max_heap[0])