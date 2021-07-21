//https://www.codewars.com/kata/554b4ac871d6813a03000035
function highAndLow(numbers){
    var nums = numbers.split(" ").map(x => parseInt(x));
    return Math.max(...nums) + " " + Math.min(...nums);
  }