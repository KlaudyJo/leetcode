class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dict = Counter(s)

        for c in t:
            dict[c] -= 1
            if dict[c] < 0:
                return False

        return True
