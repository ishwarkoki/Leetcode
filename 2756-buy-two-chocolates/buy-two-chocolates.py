class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int: 

        prices.sort() 

        newMoney = money - (prices[0]+prices[1]) 

        return newMoney if newMoney >= 0 else money
        