class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        function = [0] * 32  # function[i] = x
        # Means it will take x operations to make ith bit 1

        function[0] = 1
        for i in range(1, 32):
            function[i] = 2 * function[i - 1] + 1

        result = 0
        sign = 1

        for i in range(30, -1, -1):
            ith_bit = ((1 << i) & n)

            if ith_bit == 0:
                continue

            if sign > 0:
                result += function[i]
            else:
                result -= function[i]

            sign *= -1

        return result
