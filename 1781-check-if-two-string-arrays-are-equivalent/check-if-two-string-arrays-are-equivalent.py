class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        ans1, ans2 = '', '' 

        for word in word1: 
            ans1 += word

        for word in word2: 
            ans2 += word 

        return ans1 == ans2 
        