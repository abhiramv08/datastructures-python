#https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #Return length of min. subarray
        n = len(nums)
        min_len = n+1
        i,j = 0,0
        curr_sum = nums[0]
        while j < n:
            if curr_sum >= target:
                if (j-i+1) < min_len:
                    min_len = j-i+1
                #Move i forward until it reaches j
                while i <= j:
                    curr_sum-= nums[i]
                    i+=1
                    if curr_sum < target:
                        break
                    if (j-i+1) < min_len:
                        min_len = j-i+1
            j+=1
            if j>= n:
                break
            curr_sum+= nums[j]
        if min_len == n+1:
            return 0
        return min_len       
