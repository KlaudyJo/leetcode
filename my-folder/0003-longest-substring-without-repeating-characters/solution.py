class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        char = set()
        l = 0
        #"abcabcbb"

        for r in range((len(s))):
            while s[r] in char:
                char.remove(s[l])
                l += 1
            char.add(s[r])
            res = max(res, r-l + 1)

        return res


        
