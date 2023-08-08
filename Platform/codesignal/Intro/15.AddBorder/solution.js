// function solution(p) {
//     const a = p.map((v) => {
//         return `*${v}*`;
//     });
//     const b = '*'.repeat(a[0].length);
//     return [b, ...a, b];
// }

function solution(p) {
  const a = p.map(x => `*${x}*`)
  const b = '*'.repeat(a[0].length);
  return [b, ...a, b]
}

console.log(solution(["abc", "ded"]));