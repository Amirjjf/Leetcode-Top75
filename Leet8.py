class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:

        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False

# Example usage
s = Solution()
print(s.increasingTriplet([3, 2, 1, 0, 2, 1, 2]))  # Output: True
print(s.increasingTriplet([1, 2, 3, 4, 5]))        # Output: True
print(s.increasingTriplet([5, 4, 3, 2, 1]))        # Output: False
print(s.increasingTriplet([2, 1, 5, 0, 4, 6]))     # Output: True
