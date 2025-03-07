class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:

        dic = {}
        values = []

        for i in arr:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1

    
        # for k , v in dic.items():
        #     if v in values:
        #         return False
        #     else:
        #         values.append(v)

        
        # return True
        
        return len(dic.values()) == len(set(dic.values()))

        






solution = Solution()

arr = [1,2,2,1,1,3,0,0,0,0]
print(solution.uniqueOccurrences(arr))