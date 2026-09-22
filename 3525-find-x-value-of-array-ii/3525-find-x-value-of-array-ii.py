class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)

        tree = [(1, [0] * k) for _ in range(4 * n)]

        def merge(left, right):
            lp, lc = left
            rp, rc = right

            product = (lp * rp) % k
            cnt = lc[:]

          
            for r in range(k):
                nr = (lp * r) % k
                cnt[nr] += rc[r]

            return (product, cnt)

        def build(node, l, r):
            if l == r:
                p = nums[l] % k
                cnt = [0] * k
                cnt[p] = 1
                tree[node] = (p, cnt)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, pos, value):
            if l == r:
                p = value % k
                cnt = [0] * k
                cnt[p] = 1
                tree[node] = (p, cnt)
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(node * 2, l, mid, pos, value)
            else:
                update(node * 2 + 1, mid + 1, r, pos, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql):
            
            if r < ql:
                return None

            if ql <= l:
                return tree[node]

            mid = (l + r) // 2

            left = query(node * 2, l, mid, ql)
            right = query(node * 2 + 1, mid + 1, r, ql)

            if left is None:
                return right
            if right is None:
                return left

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:

           
            update(1, 0, n - 1, index, value)

            
            result = query(1, 0, n - 1, start)

            ans.append(result[1][x])

        return ans