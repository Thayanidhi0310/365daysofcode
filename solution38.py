class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if target > matrix[-1][-1]: return False    
        row = matrix[bisect_left(matrix, 
                  target, key = lambda x: x[-1])]   
        idx = bisect_left(row, target)             
        return row[idx] == target