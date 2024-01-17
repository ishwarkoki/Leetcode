class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool: 
        mp = Counter(arr) 

        def has_duplicates(nums): 
            hashset = set() 

            for num in nums : 
                if num in hashset : return True  
                hashset.add(num) 
            return False 
        
        return not has_duplicates(mp.values()) 


        
        