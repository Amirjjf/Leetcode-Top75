class Solution:
   def maxOperations(self, nums: list[int], k: int) -> int:
        # Dictionary to store the frequency of each number
        num_count = {}
        
        count = 0
        
        # Iterate through the array
        for num in nums:
            complement = k - num
            if complement in num_count and num_count[complement] > 0:
                count += 1
                num_count[complement] -= 1
                if num_count[complement] == 0:
                    del num_count[complement]
            else:
                if num in num_count:
                    num_count[num] += 1
                else:
                    num_count[num] = 1
        
        return count
   


   ''' 
method 2:

class Solution:
def maxOperations(self, nums: List[int], k: int) -> int:
    nums.sort()
    low = 0
    high = len(nums)-1
    count = 0
    while(low<high):
        s = nums[low]+nums[high]
        if(s<k):
            low += 1
        elif(s == k):
            count += 1
            low += 1
            high -= 1
        else:
            high -= 1
    return count


   ''' 
    



# Test the code
s = Solution()
print(s.maxOperations([1,2,3,4] , 5))