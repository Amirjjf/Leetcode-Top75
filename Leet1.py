class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        result = ""
        while word1 or word2:
            if word1:
                result += word1.pop(0)
            if word2:
                result += word2.pop(0)
        return result


# testing the solution
sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))  # apbqcr
print(sol.mergeAlternately("ab", "pqrs"))  # apbqrs
print(sol.mergeAlternately("abcd", "pq"))  # apbqcd