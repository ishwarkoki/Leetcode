class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []

        def is_arithmetic_sequence(arr) : 

            n = len(arr) 
            arr_set = set(arr)

            min_ele = min(arr) 
            max_ele = max(arr) 

            d = (max_ele - min_ele)/(n-1) 

            cur_ele = min_ele 

            while cur_ele < max_ele: 
                cur_ele = cur_ele + d 

                if cur_ele not in arr_set : 
                    return False 

            return True 

    
        for i, j in zip(l,r) : 

            ans.append(is_arithmetic_sequence(nums[i:j+1])) 

        return ans 


        