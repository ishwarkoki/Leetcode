class Solution:
    def numberOfBeams(self, bank: List[str]) -> int: 

        prev, cur, laser_count = 0, 0, 0  

        for floor in bank : 
            cur = floor.count('1') 

            laser_count += cur * prev 

            prev = cur if cur != 0 else prev 

        return laser_count 
        