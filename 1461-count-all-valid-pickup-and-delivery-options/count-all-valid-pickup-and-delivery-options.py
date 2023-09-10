class Solution:
    M = 10**9 + 7

    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1

        result = 1
        for i in range(2, n + 1):
            spaces = (i - 1) * 2 + 1
            possibility_of_i = spaces * (spaces + 1) // 2
            result *= possibility_of_i
            result %= self.M

        return result
        