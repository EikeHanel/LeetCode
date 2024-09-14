class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        data = nums1 + nums2
        data.sort()
        mid = len(data) // 2
        if not len(data) % 2:
            return (data[mid - 1] + data[mid]) / 2.0
        return data[mid]
       