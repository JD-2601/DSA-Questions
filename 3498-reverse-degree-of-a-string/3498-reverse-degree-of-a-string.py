class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i, c in enumerate(s):
            reversed_index = 26 - (ord(c) - ord('a'))
            total += reversed_index * (i + 1)
        return total