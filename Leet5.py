class Solution:
    def reverseVowels(self, s: str) -> str:
        # Convert the input string to a list for mutability
        s_list = list(s)
        
        # Define the set of vowels
        vowels = set('aeiouAEIOU')
        
        # Initialize two pointers
        left, right = 0, len(s) - 1
        
        # Loop until the two pointers meet
        while left < right:
            # Move the left pointer until it points to a vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            # Move the right pointer until it points to a vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # Swap the vowels at the left and right pointers
            s_list[left], s_list[right] = s_list[right], s_list[left]
            
            # Move both pointers towards the center
            left += 1
            right -= 1
        
        # Join the list back into a string and return
        return ''.join(s_list)

# Example usage
s = Solution()
a = s.reverseVowels("HELLO")
print(a)  # Output: HOLLE
