class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        min_heap = []
        res_map = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                heapq.heappush(min_heap, (right - left + 1, right))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            if min_heap:
                res_map[q] = min_heap[0][0]
            else:
                res_map[q] = -1
        return [res_map[q] for q in queries]
       