import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Quick sort (ramdomized)
        n = len(nums)
        if n <= 1:
            return nums
        pivotKey = random.randint(0, n-1)
        pivot = nums[pivotKey]
        nums[pivotKey], nums[n-1] = nums[n-1], nums[pivotKey]

        part1, i = 0, 0
        while i < n-1:
            if nums[i] < pivot:
                nums[i], nums[part1] = nums[part1], nums[i]
                part1+= 1
            i+= 1
        nums[n-1], nums[part1] = nums[part1], nums[n-1] #Put pivot to end of part1

        nums[:part1] = self.sortArray(nums[:part1])
        nums[part1+1:] = self.sortArray(nums[part1+1:])
        return nums
