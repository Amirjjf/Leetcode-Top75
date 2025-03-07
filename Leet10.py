class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        lastNonZeroFoundAt = 0  # Pointer to place the next non-zero element
        
        # Traverse the array and move non-zero elements to the beginning
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap the elements at lastNonZeroFoundAt and current
                nums[lastNonZeroFoundAt], nums[i] = nums[i], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1

# Example usage
s = Solution()
nums = [0, 1, 0, 3, 12]
s.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

nums = [0]
s.moveZeroes(nums)
print(nums)  # Output: [0]
