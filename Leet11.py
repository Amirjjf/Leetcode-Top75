class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si, ti = 0, 0

        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
            ti += 1

        return si == len(s)

# Test the function
s = Solution()
print(s.isSubsequence("abc", "ahbgdc"))  # Output should be True
print(s.isSubsequence("axc", "ahbgdc"))  # Output should be False
