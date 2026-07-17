class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        maxVal = max(nums)
        cnt = [0] * (maxVal + 1)
        for num in nums:
            cnt[num] += 1

        # multiplesCount[g] = kitne numbers g ke multiple hain
        multiplesCount = [0] * (maxVal + 1)
        for g in range(1, maxVal + 1):
            total = 0
            for multiple in range(g, maxVal + 1, g):
                total += cnt[multiple]
            multiplesCount[g] = total

        # exact[g] = kitne pairs ka GCD exactly g hai
        exact = [0] * (maxVal + 2)
        for g in range(maxVal, 0, -1):
            pairs = multiplesCount[g] * (multiplesCount[g] - 1) // 2
            for multiple in range(2 * g, maxVal + 1, g):
                pairs -= exact[multiple]
            exact[g] = pairs

        # prefixsum banao
        prefix = [0] * (maxVal + 2)
        for g in range(1, maxVal + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        # har query ke liye binary search se g dhoondo
        answer = []
        for q in queries:
            lo, hi = 1, maxVal
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] > q:
                    hi = mid
                else:
                    lo = mid + 1
            answer.append(lo)

        return answer