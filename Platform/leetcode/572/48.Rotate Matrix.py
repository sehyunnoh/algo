# def rotate(m):
#   result = [[0] * len(m[0]) for _ in range(len(m))]
#   for i in range(len(m)):
#     for j in range(len(m[0])):
#       result[j][len(m[0])-1-i] = m[i][j]
  
#   for i in range(len(m)):
#     for j in range(len(m[0])):
#       m[i][j] = result[i][j]
      
#   print(m)
  
# def rotate(matrix):
#     n = len(matrix)
 
#     # Transpose the matrix
#     for i in range(n):  # Iterate over the rows
#         for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
#             # Swap the elements at positions (i, j) and (j, i)
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
 
#     # Reverse each row
#     for row in matrix:  # Iterate over each row in the matrix
#         row.reverse()  # Reverse the elements in the current row
        
def rotate(m):
        for i in range(len(m)):
            for j in range(i, len(m[0])):
                m[i][j], m[j][i] = m[j][i], m[i][j]
        for row in m:
            row.reverse()   
        print(m)

rotate([[1,2,3],[4,5,6],[7,8,9]])
# rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])