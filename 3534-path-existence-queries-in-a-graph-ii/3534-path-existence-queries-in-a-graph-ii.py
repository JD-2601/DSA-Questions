class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
    
        order = sorted(range(n), key=lambda x: nums[x])
        sorted_vals = [nums[i] for i in order]
        pos = [0] * n
        for rank, node in enumerate(order):
            pos[node] = rank

        # maxReach[i] = farthest sorted-position reachable directly from i
        maxReach = [0] * n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j + 1 < n and sorted_vals[j + 1] - sorted_vals[i] <= maxDiff:
                j += 1
            maxReach[i] = j

        LOG = max(1, n.bit_length())
        jump = [maxReach]
        for k in range(1, LOG):
            prev = jump[-1]
            jump.append([prev[prev[i]] for i in range(n)])

        ans = []
        for u, v in queries:
            lo, hi = pos[u], pos[v]
            if lo > hi:
                lo, hi = hi, lo
            if lo == hi:
                ans.append(0)
                continue
            cur, steps = lo, 0
            for k in range(LOG - 1, -1, -1):
                if jump[k][cur] < hi:
                    cur = jump[k][cur]
                    steps += (1 << k)
            if jump[0][cur] >= hi:
                ans.append(steps + 1)
            else:
                ans.append(-1)
        return ans