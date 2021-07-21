//https://www.codewars.com/kata/539a0e4d85e3425cb0000a88
function add(n){
    // Let the currying begin!
    var fn = function(m){ return add(n+m); }
    fn.valueOf = function() { return n; }
    return fn;
  }