class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minheap = []

        for i in nums:
            minheap.append(i)      # Popping the elements from top of heap

        heapq.heapify(minheap)

        while len(minheap) > k:
            heapq.heappop(minheap)
                                      
        return minheap[0]

            