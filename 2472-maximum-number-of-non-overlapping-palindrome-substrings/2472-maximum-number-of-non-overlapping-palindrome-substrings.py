class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        count = 0
        i = 0

        def is_pal(sub):
            return sub == sub[::-1]

        while i <= n - k:
            if is_pal(s[i:i + k]):
                count += 1
                i += k
            elif i + k + 1 <= n and is_pal(s[i:i + k + 1]):
                count += 1
                i += k + 1
            else:
                i += 1

        return count