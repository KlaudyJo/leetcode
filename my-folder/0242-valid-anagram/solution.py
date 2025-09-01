class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        smap = {}
        sl = len(s)
        tl = len(t)

        if sl != tl:
            return False

        for i in range(sl):
            smap[s[i]] = smap.get(s[i], 0) + 1
            smap[t[i]] = smap.get(t[i], 0) - 1
        
        for c in smap.values():
            if c != 0:
                return False
        
        return True


