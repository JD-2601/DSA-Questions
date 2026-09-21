class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [0] * k
        prev = defaultdict(int)  

        for num in nums:
            cur = defaultdict(int)
            nm = num % k
            cur[nm] += 1  
            for r, cnt in prev.items():
                cur[(r * nm) % k] += cnt
            for r, cnt in cur.items():
                result[r] += cnt
            prev = cur

        return result