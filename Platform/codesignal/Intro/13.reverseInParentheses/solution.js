function solution(s) {
  while (1) {
    if (s.indexOf('(') === -1) return s;
    let start = s.lastIndexOf('(');
    let end = s.indexOf(')', start);
    s = s.slice(0, start) + s.slice(start + 1, end).split('').reverse().join('') + s.slice(end + 1)
  }
}

console.log(solution("a(bc(de))"));