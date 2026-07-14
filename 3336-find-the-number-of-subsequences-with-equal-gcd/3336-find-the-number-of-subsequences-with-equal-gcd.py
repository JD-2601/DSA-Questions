from collections import defaultdict

class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        dp = {(0, 0): 1}

        for num in nums:
            new_dp = defaultdict(int)
            for (g1, g2), cnt in dp.items():
                new_dp[(g1, g2)] = (new_dp[(g1, g2)] + cnt) % MOD

                ng1 = num if g1 == 0 else gcd(g1, num)
                new_dp[(ng1, g2)] = (new_dp[(ng1, g2)] + cnt) % MOD

                ng2 = num if g2 == 0 else gcd(g2, num)
                new_dp[(g1, ng2)] = (new_dp[(g1, ng2)] + cnt) % MOD

            dp = new_dp

        ans = 0
        for (g1, g2), cnt in dp.items():
            if g1 == g2 and g1 != 0:
                ans = (ans + cnt) % MOD
        return ans