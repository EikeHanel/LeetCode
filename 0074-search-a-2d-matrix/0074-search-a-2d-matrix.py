class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        idx = 0   
        l, r = 0, len(matrix[idx]) - 1
        for i in range(len(matrix)):
            if matrix[i][l] <= target <= matrix[i][r]:
                idx = i
                break

        print(idx)
        while l <= r:
            mid = (l + r) // 2
            if matrix[idx][mid] < target:
                l = mid + 1
            elif matrix[idx][mid] > target:
                r = mid - 1
            else:
                return True
        return False
        