class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_se = len(sentences[0].split(' '))
        for i in sentences:
            temp = len(i.split(' '))
            if temp>= max_se:
                max_se = temp
        return max_se
                
        
