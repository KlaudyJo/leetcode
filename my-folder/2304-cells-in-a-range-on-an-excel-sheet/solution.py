class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        startCol, startRow, _, endCol, endRow = s

        for j in range(ord(startCol), ord(endCol) + 1):
            for i in range(int(startRow), int(endRow) + 1):
                ans.append(chr(j) + str(i))

        return ans

