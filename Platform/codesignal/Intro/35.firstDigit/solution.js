// function solution(s) {
//     let arr = s.split('');
//     for (let i = 0; i < arr.length; i++) {
//         if (arr[i].charCodeAt() >= 48 && arr[i].charCodeAt() <= 57) {
//             return arr[i];
//         }
//     }
// }

// function solution2(s) {
//     return s.match(/\d/)[0]
// }

// function solution3(s) {
//     return s.match(/[0-9]/)[0]
// }

function solution4(s) {
  for (let i = 0; i < s.length; i++) {
    if (s[i] >= "0" && s[i] <= "9") {
      return s[i];
    }
  }
}

console.log(solution("var_1__Int"));