class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        sl = len(s)
        tl = len(t)
        
        if sl != tl:
            return False
        
        for i in range(sl):
            smap[s[i]] = smap.get(s[i], 0) + 1
            smap[t[i]] = smap.get(t[i], 0) - 1
        
        for count in smap.values():
            if count != 0:
                return False
        
        return True
        
