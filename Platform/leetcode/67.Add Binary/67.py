class Solution:
  def addBinary(self, a:str, b:str) -> str:
    max_len = max(len(a), len(b))
    if len(a) != max_len:
      a = a.rjust(max_len, '0')
    else:
      b = b.rjust(max_len, '0')
    print(a,b)
    carry = 0
    result = ''
    for i in range(len(a)-1, -1, -1):
      sum = int(a[i]) + int(b[i]) + carry
      if sum > 2:
        carry = 1
        result = '1' + result
      elif sum == 2:
        carry = 1
        result = '0' + result
      else:
        carry = 0
        result = str(sum) + result
    if carry:
      result = '1' + result
    return result


# class Solution:
#   def addBinary(self, a:str, b:str) -> str:
#     return str(bin(int(a, 2) + int(b, 2)))[2:]

s = Solution()
print(s.addBinary("11","1")) # 100