class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0  # Pointer to write the compressed characters
        read = 0  # Pointer to read the original characters
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            
            # Count the occurrences of the current character
            while read < n and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write

# Example usage
s = Solution()
chars = ["a","a","b","b","c","c","c"]
new_length = s.compress(chars)
print(new_length)  # Output: 6
print(chars[:new_length])  # Output: ['a', '2', 'b', '2', 'c', '3']

chars = ["a"]
new_length = s.compress(chars)
print(new_length)  # Output: 1
print(chars[:new_length])  # Output: ['a']

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
new_length = s.compress(chars)
print(new_length)  # Output: 4
print(chars[:new_length])  # Output: ['a', 'b', '1', '2']
