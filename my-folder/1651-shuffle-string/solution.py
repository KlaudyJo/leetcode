class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        N = len(s)
        A = [0] * N
    
        for ix, c in zip(indices, s):
            A[ix] = c
        return "".join(A)
