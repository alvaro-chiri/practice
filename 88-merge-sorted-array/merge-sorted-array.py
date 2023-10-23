class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = m+n
        n = n -1

        while m < length:
            if nums1[m] == 0:
                nums1[m] = nums2[n]
                n-=1
            m += 1
        
        nums1.sort()