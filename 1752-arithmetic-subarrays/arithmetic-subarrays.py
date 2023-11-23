class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []

        def is_arithmetic_sequence(arr) : 

            arr.sort()

            d = arr[1] - arr[0] 

            for i in range(2,len(arr)): 
                if arr[i] - arr[i-1] != d : 
                    return False 

            return True 

    
        for i, j in zip(l,r) : 

            ans.append(is_arithmetic_sequence(nums[i:j+1])) 

        return ans 


        