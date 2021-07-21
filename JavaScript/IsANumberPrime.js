//https://www.codewars.com/kata/5262119038c0985a5b00029f

function isPrime(num) {
    if (num > 2 && num % 2 == 0) return false;
    for (var i = 3; i*i <= num; i = i+2) if (num % i == 0) return false;
    return num >= 2;
  }
  
  //Previous Solution
/*
function isPrime(num) {
  if (num == 2 || num == 3) return true;
  if ((num < 2) || (num % 2) == 0 || (num % 3) == 0) return false;
  for (var i = 5; i*i <= num; i = i+2){
    if ((num % i) == 0) return false;
  }
  return true;
}
*/