class Solution:
    def integerBreak(self, n: int) -> int:
        
        def solve(n, memo = {}): 

            if n in memo:
                return memo[n]
            if n == 2:
                return 1
            max_product = 0
            
            for i in range(1, n):
                # Calculate the product of breaking n into i and (n - i)
                product = i * (n - i)
                # Recursively calculate the product for (n - i)
                remaining_product = i * solve(n - i)
                # Take the maximum of the current product and remaining_product
                max_product = max(max_product, max(product, remaining_product))
            
            memo[n] = max_product
            return memo[n]

        return solve(n) 
    


 

     



    


       