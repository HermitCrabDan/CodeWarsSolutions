//https://www.codewars.com/kata/563b662a59afc2b5120000c6
function nbYear(p0, percent, aug, p) {
    // your code
    y = 0
    while (p0 < p) {
      p0 = p0 * (1+percent/100.0) + aug;
      y++;
    }
    return Math.ceil(y);
}