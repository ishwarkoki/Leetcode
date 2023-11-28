class Solution:
    def numberOfWays(self, corridor: str) -> int:
        pos_seats = []
        mod = 10**9+7

        for i in range(len(corridor)):
            if corridor[i] == 'S':
                pos_seats.append(i)

        if len(pos_seats) % 2 or len(pos_seats) == 0:
            return 0

        result = 1
        prev = pos_seats[1]  # End index of the starting subarray having 2 seats

        for i in range(2, len(pos_seats), 2):
            length = pos_seats[i] - prev
            result = (result * length) % mod 

            prev = pos_seats[i + 1]

        return result
        