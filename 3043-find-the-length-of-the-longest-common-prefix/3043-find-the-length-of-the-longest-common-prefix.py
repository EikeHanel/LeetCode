class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        prefix_set = set() 
        for n in arr1:
            while n:
                prefix_set.add(n)
                n = n // 10
        ans = 0
        for k in arr2:
            while k and k not in prefix_set:
                k = k // 10
            if k:
                ans = max(ans, len(str(k)))
        return ans
        