//https://www.codewars.com/kata/53db96041f1a7d32dc0004d2
function doneOrNot(board){
    //your code here
    var error = "Try again!";
    var result = "Finished!";
    board.forEach(r => { r.slice().sort().forEach((f,i)=>{ if(f != i+1) result = error; }); });
    for (var c = 0; c < 9; c++){
      var cols = [];
      board.forEach(b => { cols.push(b[c]); });
      cols.sort().forEach((f,i) => { if (f != i+1) result = error; });
      var reg = []; var row = 0; var col = 3*(c%3);
      if (c > 6) row = 6;
      else if (c > 3) row = 3;
      for (var j = 0; j < 9; j++){
        //console.log('r'+row+' c'+col);
        reg.push(board[row][col]);
        if ((j+1)%3 == 0) { row++; col = col-2; }
        else col++;
      }
      reg.sort().forEach((f,i) => { if (f != i+1) result = error; });
    }
    return result;
  }