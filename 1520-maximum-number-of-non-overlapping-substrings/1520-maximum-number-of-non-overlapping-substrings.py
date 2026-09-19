class Solution(object):
    def maxNumOfSubstrings(self, s):
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        
        intervals = []
        for c in first:
            start = first[c]
            end = last[c]
            i = start
            valid = True
            while i <= end:
                if first[s[i]] < start:
                    valid = False
                    break
                if last[s[i]] > end:
                    end = last[s[i]]
                i += 1
            if valid:
                intervals.append((start, end))

       
        intervals.sort(key=lambda x: x[1])
        res = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end

        return res