class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        freq = defaultdict(int)
        freq[0] = 1
        count = 0
        total = 0

        for n in nums:
            total += n
            count += freq[total - k]
            freq[total] += 1

        return count


