class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsIdx = {n:i for i,n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        #[1,3,4,2]
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = numsIdx[val]
                res[idx] = curr
            if curr in numsIdx:
                stack.append(curr)

        return res

