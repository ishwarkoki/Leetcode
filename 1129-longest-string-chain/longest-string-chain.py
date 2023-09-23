class Solution: 
    def longestStrChain(self,words):
        words.sort(key=len)
        n = len(words)
        
        # Initialize an array to store the length of the longest chain ending at each word
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if self.isPredecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Find the maximum value in dp
        max_chain_length = max(dp)
        
        return max_chain_length

    def isPredecessor(self,word1, word2):
        if len(word1) + 1 != len(word2):
            return False
        i = j = 0
        found_difference = False
        while i < len(word1) and j < len(word2):
            if word1[i] != word2[j]:
                if found_difference:
                    return False
                found_difference = True
                j += 1
            else:
                i += 1
                j += 1
        return True
