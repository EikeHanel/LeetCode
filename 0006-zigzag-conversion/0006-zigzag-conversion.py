class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of empty strings for each row
        rows = [''] * numRows
        print(rows)
        cur_row = 0
        going_down = False

        # Set char to fitting row
        for char in s:
            rows[cur_row] += char
            print(f"row: {cur_row} val: {rows}")
            # Change direction if we reach the top or bottom row
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            if going_down:
                cur_row += 1
            else:
                cur_row -= 1

        # Concatenate all rows to get the final result
        return ''.join(rows)