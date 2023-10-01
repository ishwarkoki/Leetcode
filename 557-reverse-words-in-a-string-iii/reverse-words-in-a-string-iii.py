class Solution:
    def reverseWords(self, s: str) -> str: 
        strArray = s.split(" ") 
        print(strArray)
        ans = []

        for word in strArray : 
            ans.append(word[::-1])

        return ' '.join(ans)

        