class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq

        heap = []

        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            elif n > heap[0]:
                heapq.heapreplace(heap, n)

        return heap[0]


