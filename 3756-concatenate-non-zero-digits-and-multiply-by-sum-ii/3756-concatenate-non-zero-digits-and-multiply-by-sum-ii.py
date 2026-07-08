class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
    
        MOD = 10**9 + 7
        n = len(s)
        
       
        cnt = [0] * (n + 1)      
        val = [0] * (n + 1)      
        digit_sum = [0] * (n + 1)  
        
        for i in range(n):
            d = int(s[i])
            if d != 0:
                cnt[i+1] = cnt[i] + 1
                val[i+1] = (val[i] * 10 + d) % MOD
                digit_sum[i+1] = digit_sum[i] + d
            else:
                cnt[i+1] = cnt[i]
                val[i+1] = val[i]
                digit_sum[i+1] = digit_sum[i]
        
        
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
        
        answer = []
        for l, r in queries:
            k = cnt[r+1] - cnt[l] 
            x_mod = (val[r+1] - val[l] * pow10[k]) % MOD
            s_sum = digit_sum[r+1] - digit_sum[l]
            result = (x_mod * s_sum) % MOD
            answer.append(result)
        
        return answer