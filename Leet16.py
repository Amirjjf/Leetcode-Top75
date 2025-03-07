class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = right = 0
        max_length = 0
        zeroes = 0

        while right < len(nums):
            if nums[right] == 0:
                zeroes += 1
            
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length

# Test the function
s = Solution()
print(s.longestOnes([1, 0, 1, 0, 0, 1, 0, 0, 0], 2))
