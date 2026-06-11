def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return True
    return False
    
print(searchMatrix(matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10))