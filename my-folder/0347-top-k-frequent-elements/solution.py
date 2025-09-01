class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_map = {}

        for i, n in enumerate(nums):
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        
        sorted_items = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]
        
