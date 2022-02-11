class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # sol = [1]*(len(nums))
        # pre = 1
        # for i in range(len(nums)):
        #     sol[i] = pre
        #     pre *= nums[i]
        # post = 1
        # for i in range(len(nums) -1,-1,-1):
        #     sol[i] *= post
        #     post *= nums[i]
        # return sol
        p = [1] * len(nums); backward = 1
        for i in range(1, len(nums)):
            p[i] = p[i-1] * nums[i - 1]
        for i in range(len(nums)-1, -1, -1):
            p[i] *= backward
            backward *= nums[i]
        return p
