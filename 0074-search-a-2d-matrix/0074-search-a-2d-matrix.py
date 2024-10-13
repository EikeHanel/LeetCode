class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        target_row = 0
        while top <= bot:
            mid_row = (top + bot) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                target_row = mid_row
                break
        if not (top <= bot):
            return False

        l, r = 0, len(matrix[target_row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[target_row][mid] < target:
                l = mid + 1
            elif matrix[target_row][mid] > target:
                r = mid - 1
            else:
                return True
        return False
        