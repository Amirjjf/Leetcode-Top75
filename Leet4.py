class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0  # Number of flowers planted
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:  # Check if current plot is empty
                # Check if left and right plots are empty or out of bounds
                empty_left = (i == 0 or flowerbed[i - 1] == 0)
                empty_right = (i == length - 1 or flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    # Plant a flower here
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        
        return count >= n

s = Solution()

print(s.canPlaceFlowers([1,0,0,0,1], 1))
