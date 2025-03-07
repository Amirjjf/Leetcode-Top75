class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        max_alt = 0
        gain.insert(0,0)
        length = len(gain)
        new_list = [0] * length 

        for i in range(1 , length):
            new_list[i] = gain[i] + new_list[i-1]
            max_alt = max(max_alt , new_list[i])
        
        return max_alt




s = Solution()
print(s.largestAltitude([-5,1,5,0,-7]))
        