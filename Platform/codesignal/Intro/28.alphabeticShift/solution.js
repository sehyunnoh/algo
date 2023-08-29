function solution(s){
  return s.split("").map(x => (x.charCodeAt(0) > 121) ? 'a' : String.fromCharCode(x.charCodeAt(0) + 1)).join("")
}

function solution(s) {
  var c="abcdefghijklmnopqrstuvwxyza"
  return s.replace(/./g,x=>c[c.indexOf(x)+1])
}

console.log(solution("crazy"));