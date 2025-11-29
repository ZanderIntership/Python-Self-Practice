class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        NewArray = []
        middlepoint = 0

        for i in range(len(nums1)):
            NewArray.append(nums1[i])
        
        for j in range(len(nums2)):
            NewArray.append(nums2[j])

        MedianValue = statistics.median(NewArray) 
        return MedianValue
