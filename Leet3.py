class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        max_candies = max(candies)  # Use max() to find the maximum number of candies directly
        
        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result


s = Solution()

a = s.kidsWithCandies([2,3,5,3,2], 2)
print(a)