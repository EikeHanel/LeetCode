class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def dfs(i, j, count):
            curr_count = 0
            for n in range(len(arr1)):
                for k in range(len(arr2)):
                    if str(arr1[n])[i:j] == str(arr2[k])[i:j]:
                        curr_count = max(count, j)
                        print(f"IF count: {curr_count}")
                        return dfs(i, j+1, curr_count)
            print(f"END count: {curr_count}")
            return max(curr_count, j-1)

        return dfs(0, 1, 0)
