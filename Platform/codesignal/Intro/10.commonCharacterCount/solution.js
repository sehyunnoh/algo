function solution(s1, s2) {
  let max = 0

  let set = new Set()
  s1.split("").forEach(x => set.add(x))
  set.forEach(x => {
    let s1Cnt = s1.split("").filter(y=>y===x).length
    let s2Cnt = s2.split("").filter(y=>y===x).length

    max += Math.min(s1Cnt, s2Cnt)
  })
  return max
}

console.log(solution("aabcc", "adcaa"));