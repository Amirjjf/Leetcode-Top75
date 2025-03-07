class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

        s1 , s2 = set(nums1), set(nums2)
        answer_list = [[], []]

        for i in s1: 
            if i not in s2:
                answer_list[0].append(i)

        
        for i in s2:
            if i not in s1:
                answer_list[1].append(i)


        return answer_list
    



nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

solution = Solution()
print(solution.findDifference(nums1 , nums2))

        