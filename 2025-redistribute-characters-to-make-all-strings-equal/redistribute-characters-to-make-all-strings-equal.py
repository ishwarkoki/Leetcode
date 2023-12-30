class Solution:
    def makeEqual(self, words: List[str]) -> bool: 

        freq_map = defaultdict(int) 
        n = len(words) 

        for word in words : 
            for char in word : 
                freq_map[char] += 1 


        for key, val in freq_map.items() : 
            if val % n != 0 : return False 


        return True 


        