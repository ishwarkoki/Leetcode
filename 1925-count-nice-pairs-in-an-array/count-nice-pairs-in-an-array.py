class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7  
        ans = 0 

        def rev(num): 
            rev_num = 0 

            while num: 

                rev_num = rev_num*10 + num % 10 
                num //= 10 

            return rev_num

        hashmap = defaultdict(int)  

        for i, num in enumerate(nums): 
            value = num - rev(num)

            if value in hashmap : 
                ans += hashmap[value]  
                
            hashmap[value] += 1 

        return ans % MOD

            

                


        



        




        