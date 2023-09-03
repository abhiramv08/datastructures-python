class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #Merge sort
        n = len(nums)
        if n == 1:
            return nums
        if n == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
            return nums
        mid = ceil(n/2) - 1
        nums1, nums2 = self.sortArray(nums[:mid+1]), self.sortArray(nums[mid+1:])
        i,j,k = 0,0,0
        while j < len(nums1) and k < len(nums2):
            if nums1[j] < nums2[k]:
                nums[i] = nums1[j]
                j+=1
            else:
                nums[i] = nums2[k]
                k+=1
            i+=1
        while j < len(nums1):
            nums[i] = nums1[j]
            j+=1
            i+=1
        while k < len(nums2):
            nums[i] = nums2[k]
            k+=1
            i+=1
        return nums
            
