class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]: 
        m = len(flowers)
        n = len(people)

        result = [0] * n

        start_time = [flower[0] for flower in flowers]
        end_time = [flower[1] for flower in flowers]

        start_time.sort()
        end_time.sort()

        for i in range(n):
            bloomed_already = self.upper_bound(start_time, people[i]) - self.lower_bound(end_time, people[i])
            result[i] = bloomed_already

        return result

    def upper_bound(self, arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    def lower_bound(self, arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
        