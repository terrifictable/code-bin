const readline = require("readline-sync");

const arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];

function binary_search(target, start, end) {
  if (start > end) {
    return "Not Found";
  }
  const middle = Math.floor((start + end) / 2);

  if (arr[middle] === target.toLowerCase()) {
    return `Letter ${target} is the ${middle + 1}th number in alphabet`;
  }

  if (arr[middle] > target.toLowerCase()) {
    return binary_search(target, start, middle - 1);
  }
  if (arr[middle] < target.toLowerCase()) {
    return binary_search(target, middle + 1, end);
  }
}

to_find = readline.question("Character to find in alphabet >>> ");
console.log(binary_search(to_find, 0, arr.length));
