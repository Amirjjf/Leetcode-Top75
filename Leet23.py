class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:

        rotated_grid = [[] for _ in range(len(grid))]
        
     
        j = 0
        while j < len(grid):
            for i in range(len(grid)):
                rotated_grid[j].append(grid[i][j])
            j += 1

        count = 0
        p1 = 0
        while p1 < len(grid):
            p2 = 0
            while p2 < len(grid):
                if grid[p1] == rotated_grid[p2]:
                    count += 1
                p2 += 1
            p1 += 1

        return count
    


# Faster Solution

    
# class Solution:
#     def equalPairs(self, grid: list[list[int]]) -> int:
        
#         row_dict = {}
#         for row in grid:
#             row_tuple = tuple(row)
#             row_dict[row_tuple] = row_dict.get(row_tuple,0) + 1

#         col_dict = {}
#         for col in range(len(grid)):
#             column_value = []
#             for row in range(len(grid)):
#                 column_value.append(grid[row][col])
#             col_tuple = tuple(column_value)
#             col_dict[col_tuple] = col_dict.get(col_tuple,0) + 1
        
#         count = 0
#         for col_tuple, col_count in col_dict.items():
#             if col_tuple in row_dict:
#                 count += col_count * row_dict[col_tuple]
#         return count



grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]
solution = Solution()
print(solution.equalPairs(grid))