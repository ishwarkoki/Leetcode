class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: 
        nums = [] 
        i, j = 0, 0 
        m, n = len(nums1), len(nums2) 

        while i<m and j<n :  
            if nums1[i] <= nums2[j] : 
                nums.append(nums1[i]) 
                i += 1 

            else : 
                nums.append(nums2[j]) 
                j += 1 

        while i < m : 
            nums.append(nums1[i]) 
            i += 1
        
        while j < n : 
            nums.append(nums2[j]) 
            j += 1  

        print(nums)

        length = m+n 

        if length % 2 == 0 : 
            return (nums[length//2] + nums[length//2 -1])/2 

        else : 
            return nums[length//2] 


        

        




            

        
        

        

            




        