from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False

        
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        print(freq1.values())

        
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        
        return sorted(freq1.values()) == sorted(freq2.values())



# Test case
word1 = "abcaaz"
word2 = "abcazz"
solution = Solution()
print(solution.closeStrings(word1, word2))  # Expected output: True
