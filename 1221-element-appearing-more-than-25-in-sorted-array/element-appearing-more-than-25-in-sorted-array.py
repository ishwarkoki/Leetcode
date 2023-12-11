class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int: 
        arr_count = Counter(arr) 
        twenty_five_percent = len(arr)/4 

        for key, value in arr_count.items(): 
            if value > twenty_five_percent: return key 

        

        