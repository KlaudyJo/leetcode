class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10

        count = 10
        digits = 9
        avaible = 9

        for i in range(2, n+1):
            digits *=  avaible
            count += digits
            avaible -= 1

        return count
        


                
