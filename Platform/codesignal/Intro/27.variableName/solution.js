function solution(name) {
  if (!isNaN(name[0])) return false;
  return name.split("").map(x => {
    if (x === '_') return true;
    if (x >= '0' && x <= '9') return true;
    if (x.toLowerCase() >= 'a' && x.toLowerCase() <= 'z') return true;
    return false;
  }).every(x => x);
}

function solution(name) {
  if(!isNaN(name[0])) return false;
  if(name.length != name.match(/[a-zA-Z_\d]+/)[0].length) return false;
  return true;
}

function solution(name) {
  return /^[a-z_]\w*$/i.test(name)
}


console.log(solution("var_1__Int"));