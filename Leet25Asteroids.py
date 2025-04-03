class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if abs(a) > abs(stack[-1]):
                    stack.pop()  
                elif abs(a) == abs(stack[-1]):
                    stack.pop() 
                    break
                else:
                    break  
            else:
                stack.append(a)

        return stack


# Example usage
solution = Solution()
print(solution.asteroidCollision([-2, -1, 1, 2]))  
