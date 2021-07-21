//https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
snail = function(array) {
    var ret = [];
    var n = array[0].length;
    var row = 0;
    var col = 0;
    var passes = 0;
    var direction = 0;
    for (var i = 0; i < n*n; i++){
        ret.push(array[row][col]);
      if (direction == 0){
        if (col == n-1-passes) { direction++; row++ } else {col++}
      } else if (direction == 1){
        if (row == n-1-passes) { direction++; col--;} else {row++}
      } else if (direction == 2){
        if (col == passes){ direction++; row--;} else {col--}
      } else {
        if (row == passes+1) { direction = 0; col++; passes++} else {row--}
      }
    }
    return ret;
  }