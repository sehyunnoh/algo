class Solution:
  def addBinary(self, a:str, b:str) -> str:
    max_len = max(len(a), len(b))
    if len(a) != max_len:
      a = a.rjust(max_len, '0')
    else:
      b = b.rjust(max_len, '0')
    print(a,b)
    add = 0
    result = ''
    for i in range(len(a)-1, -1, -1):
      sum = int(a[i]) + int(b[i]) + add
      if sum > 2:
        add = 1
        result = '1' + result
      elif sum == 2:
        add = 1
        result = '0' + result
      else:
        add = 0
        result = str(sum) + result
    if add:
      result = '1' + result
    return result

s = Solution()
print(s.addBinary("11","1")) # 100