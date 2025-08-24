class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums: 
            return []

        if nums[0] > 0:
            return [n**2 for n in nums]

        m =len(nums)
        for i,n in enumerate(nums):
            if n>=0:
                m=i
                break

        A,B = nums[m:], [i*-1 for i in reversed(nums[:m])]
        res = []
        a=b=0
        while a < len(A) and b < len(B):
            if A[a] < B[b]:
                res.append(A[a])
                a += 1
            else:
                res.append(B[b])
                b += 1
        if a < len(A):
            res.extend(A[a:])
        else:
            res.extend(B[b:])

        return [n**2 for n in res]
