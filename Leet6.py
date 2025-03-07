class Solution:
    def reverseWords(self, s: str) -> str:

        # rev = s.strip().split(" ")
        # new = []
        # for i in rev: 
        #     if i != '':
        #         new.append(i)
        # s = " ".join(new[::-1])
        # return s
    

    # second way:
        words = [word for word in s.strip().split() if word]
        # Join the words with a single space and return the result
        return " ".join(words[::-1])


s = Solution()
print(s.reverseWords("a good   example"))
