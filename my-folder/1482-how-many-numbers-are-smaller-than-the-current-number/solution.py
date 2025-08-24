class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        dct = {}

        for i,n in enumerate(temp):
            if n not in dct:
                dct[n] = i
        
        res = []

        for i in nums:
            res.append(dct[i])
        return res
            
