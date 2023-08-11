function solution(s) {
  set = new Set(s)
  let num = []
  for (let x of set) {
    let count = 0
    for (let i = 0; i < s.length; i++) {
      if(x === s[i]) count++;
    }
    num.push(count)
  }
  return num.filter(x => x % 2 === 1).length <= 1
}

function solution(str) {
  let obj = {};
  for (let i = 0; i < str.length; i++) {
    if (str[i] in obj) {
      obj[str[i]]++;
    } else {
      obj[str[i]] = 1;
    }
  }

  let cnt = 0;
  for (let [key, value] of Object.entries(obj)) {
    if (value % 2 !== 0) cnt++;
    if (cnt > 1) return false;
  }
  return true;
}

console.log(solution("aabb"));