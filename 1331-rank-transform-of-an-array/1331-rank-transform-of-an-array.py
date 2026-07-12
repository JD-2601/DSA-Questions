class Solution(object):
    def arrayRankTransform(self, arr):
        arr1 = sorted(arr)
        result = []
        rank = {}
        n=1
        for i in range(len(arr1)):
            if i>0 and arr1[i] == arr1[i-1]:
                rank[arr1[i]] = n-1
            else:
                rank[arr1[i]] = n
                n=n+1
        for x in arr:
            result.append(rank[x])
        return result

            
