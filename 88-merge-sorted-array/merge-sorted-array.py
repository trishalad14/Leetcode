class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:]=nums2
        def insertion_sort(nums1):
            size=len(nums1)
            for i in range(1,size):
                key=nums1[i]
                j=i-1
                while j>=0 and nums1[j]>key:
                    nums1[j+1]=nums1[j]
                    j-=1
                nums1[j+1]=key 
        insertion_sort(nums1) 
        
      


        