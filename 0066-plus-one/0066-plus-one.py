class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        integer = int("".join(map(str,digits)))
        integer+=1
        integer = list(str(integer))
        return list(map(int,integer))
