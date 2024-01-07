class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        count = 0

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                count += dp[j][diff]  # Add the number of arithmetic slices ending at i

        return count 

        