class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack
        




solution = Solution()
print(solution.asteroidCollision([-2,-1,1,2]))
        