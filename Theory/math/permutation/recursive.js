function generatePermutations(arr) {
  const result = [];

  function permute(currentArr, remainingArr) {
    if (remainingArr.length === 0) {
      result.push(currentArr);
      return;
    }

    for (let i = 0; i < remainingArr.length; i++) {
      const newArr = currentArr.concat(remainingArr[i]);
      const newRemainingArr = remainingArr.slice(0, i).concat(remainingArr.slice(i + 1));
      permute(newArr, newRemainingArr);
    }
  }

  permute([], arr);

  return result;
}

const inputArray = [1, 2, 3];
const permutations = generatePermutations(inputArray);
console.log(permutations);