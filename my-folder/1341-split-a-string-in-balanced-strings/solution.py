class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        check = {'R': 0, 'L': 0}
        count=0
        for word in s:
            check[word] += 1
            if check['R'] == check['L']:
                count += 1
                check['R'] = 0
                check['L'] = 0
        return count
