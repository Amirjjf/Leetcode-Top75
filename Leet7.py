class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        # Initialize prefix and suffix arrays
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n
        
        # Compute prefix products
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # Compute suffix products
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # Compute the result array
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        
        return result

# Example usage
s = Solution()
result = s.productExceptSelf([1, 2, 3, 4])
print(result)  # Output: [24, 12, 8, 6]
