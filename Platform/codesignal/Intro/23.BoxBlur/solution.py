def solution(image):
  row, col = len(image)-2, len(image[0])-2
  result = [[0 for _ in range(col)] for _ in range(row)]
  for r in range(row):
    for c in range(col):
      result[r][c] = (
        (image[r][c] + image[r][c+1] + image[r][c+2] +
         image[r+1][c] + image[r+1][c+1] + image[r+1][c+2] +
         image[r+2][c] + image[r+2][c+1] + image[r+2][c+2])//9
      )
  return result

def solution(m):
    r = len(m)
    c = len(m[0])
    ans = []
    for i in range(1,r-1):
        row=[]
        for j in range(1,c-1):
            row.append(sum([m[i+k][j+l] for k in [-1,0,1] for l in [-1,0,1]])//9)
        ans.append(row)
    return ans

def solution(image):
    return [[int(sum(sum(x[i:i+3]) for x in image[j:j+3])/9) for i in range(len(image[j])-2)] for j in range(len(image)-2)]

print(solution([[1,1,1], 
 [1,7,1], 
 [1,1,1]]))