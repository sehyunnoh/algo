function generatePermutations(arr) {
  const result = [];
  const n = arr.length;
  const c = new Array(n).fill(0);

  result.push([...arr]);

  let i = 0;
  while (i < n) {
    if (c[i] < i) {
      if (i % 2 === 0) {
        [arr[0], arr[i]] = [arr[i], arr[0]];
      } else {
        [arr[c[i]], arr[i]] = [arr[i], arr[c[i]]];
      }

      result.push([...arr]);
      c[i]++;
      i = 0;
    } else {
      c[i] = 0;
      i++;
    }
  }

  return result;
}

const inputArray = [1, 2, 3];
const permutations = generatePermutations(inputArray);
console.log(permutations);