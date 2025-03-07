class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_water = width * current_height
            max_water = max(max_water, current_water)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

# Test the function
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))  # Output should be 49
