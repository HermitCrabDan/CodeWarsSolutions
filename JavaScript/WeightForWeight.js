//https://www.codewars.com/kata/55c6126177c9441a570000cc
function orderWeight(strng) {
    return strng.split(" ").sort(function(a,b) {
      if (sumChars(a) > sumChars(b)) return 1;
      if (sumChars(a) == sumChars(b) && a > b) return 1;
      return - 1;
    }).join(" ");
}
function sumChars(str){
  return str.split('').map(x => Number(x)).reduce(function(t,n){ return t+n;});
}