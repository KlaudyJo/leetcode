class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x % 10 == 0 & x!=0):
            return False
        number =x
        reverse = 0
        while number:
            reverse = reverse*10 + number%10
            number //=10
        return x == reverse
        
