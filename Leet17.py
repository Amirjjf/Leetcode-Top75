class Solution:
    def longestSubarray(self, nums: list[int]) -> int:

        left = right = 0
        max_length = 0
        zeroes = 0

        while right < len(nums):

            if nums[right] == 0:
                zeroes += 1
            
            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length - 1






s = Solution()
print(s.longestSubarray([1,1,1,0,1,1,1,1]))