class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):

            right_sum = total_sum - left_sum - nums[i]
            
            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1




s = Solution()
print(s.pivotIndex([1,3,7,6,6,5]))
        