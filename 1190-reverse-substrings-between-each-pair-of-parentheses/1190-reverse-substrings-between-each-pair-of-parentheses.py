class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if c == ')':
                portion = []
                while stack[-1] != '(':
                    portion.append(stack.pop())
                stack.pop()
                stack.extend(portion)
            
            else:
                stack.append(c)

        return "".join(stack)