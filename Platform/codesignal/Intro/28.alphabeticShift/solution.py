def solution(s):
  return "".join(['a' if (ord(x)+1) > 122 else chr(ord(x)+1) for x in s])

def solution(s):
    return "".join(chr((ord(i)-96)%26+97) for i in s)

print(solution("crazy"))