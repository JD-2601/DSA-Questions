class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        cur_dep = 0
        for c in s:
            if c == '(':
                cur_dep += 1 
            elif c == ')':
                cur_dep -= 1
            res = max(res,cur_dep)

        return res