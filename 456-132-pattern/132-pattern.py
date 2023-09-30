class Solution:
    def find132pattern(self, nums):
        stack = []  # decreasing stack
        ak = float('-inf')  # We want to find a seq ai < ak < aj.

        for num in reversed(nums):
            # ai < ak, we're done because ai must also be smaller than aj.
            if num < ak:
                return True
            while stack and stack[-1] < num:
                ak = stack.pop()
            stack.append(num)  # num is a candidate of aj.

        return False
