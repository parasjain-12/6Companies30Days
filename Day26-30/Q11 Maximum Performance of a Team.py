import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = [(speed[i],efficiency[i]) for i in range(n)]
        engineers.sort(key = lambda x : (-x[1],x[0]))
        result = 0
        heap = []
        totalSum = 0
        for i in range(n):
            while len(heap) >= k:
                totalSum -= heapq.heappop(heap)
            result = max(result , (totalSum + engineers[i][0]) * engineers[i][1] )
            heapq.heappush(heap,engineers[i][0])
            totalSum += engineers[i][0]
        return result % (10 ** 9 + 7)
