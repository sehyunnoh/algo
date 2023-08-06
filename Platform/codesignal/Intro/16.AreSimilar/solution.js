// function solution(a, b) {
//   if ([...a].sort().toString() !== [...b].sort().toString()) return false;
//   let diff = 0;
//   for(let i=0; i<a.length; i++) {
//     if (a[i] !== b[i]) diff++;
//     if (diff > 2) return false;
//   }
//   return true;
// }


// function solution(a,b) {
//   let result = [];
//   let diff = 0;

//   a.forEach((v, i) => {
//     if (v !== b[i]) {
//       result.push(v);
//       result.push(b[i]);
//       diff++;
//       if (diff > 2) return false;
//     }
//   })
//   return diff === 0 || (diff === 2 && result[0] === result[3] && result[1] === result[2])
// }

// function solution(a, b) {
//   aC=[...a];
//   bC=[...b];
//   a.sort();
//   b.sort();
//   arr=[];
//   num=0;
//   if(a.length == b.length) {
//       for(i=0; i<a.length; i++) {
//           if(a[i] != b[i]) return false;
//           if(aC[i] != bC[i]) num++; 
//       }if(num > 2) return false; 
//       return true;
//   }return false; 
// }

// function solution(a,b) {
//   let result = true;
//   let diff = [];
//   a.forEach((v, i) => {
//     if (v !== b[i]) diff.push(i);
//   });
//   if (diff.length === 0) return true;
//   if (diff.length === 2) {
//     let temp = a[diff[0]];
//     a[diff[0]] = a[diff[1]];
//     a[diff[1]] = temp;
//     if (a.toString() === b.toString()) return true;
//   }
//   return false;
// }

console.log(solution([1, 2, 1, 2], [2, 2, 1, 1]));
console.log(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]));
console.log(solution([832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]));