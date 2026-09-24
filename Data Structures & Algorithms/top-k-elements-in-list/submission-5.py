import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        minheap = []
        for key, val in count.items():
            heapq.heappush(minheap, (val, key))
            heapq.heapify(minheap)

            if len(minheap) > k:
                minheap.pop(0)
        
        return [key for (val, key) in minheap]