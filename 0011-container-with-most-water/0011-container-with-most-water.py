class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            # Calculate the area with the current pair of lines
            width = right - left
            height_min = min(height[left], height[right])
            water_current = height_min * width
            # Update the maximum water found
            max_water = max(max_water, water_current)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
