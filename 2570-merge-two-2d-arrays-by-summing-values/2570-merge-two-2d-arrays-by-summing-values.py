class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        l, r = 0, 0
        res = []

        while l < len(nums1) and r < len(nums2):
            if nums1[l][0] == nums2[r][0]:
                res.append([nums1[l][0], nums1[l][1] + nums2[r][1]])
                l += 1
                r += 1
            elif nums1[l][0] < nums2[r][0]:
                res.append([nums1[l][0], nums1[l][1]])
                l += 1
            elif nums1[l][0] > nums2[r][0]:
                res.append([nums2[r][0], nums2[r][1]])
                r += 1
            
        if l < len(nums1):
            for p in nums1[l:]:
                res.append(p)
        if r < len(nums2):
            for p in nums2[r:]:
                res.append(p)

        return res