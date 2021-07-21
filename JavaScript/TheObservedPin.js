//https://www.codewars.com/kata/5263c6999e0f40dee200059d
function getPINs(observed) {
    var alts = [[8],[2,4],[1,3,5],[2,6],[1,5,7],[2,4,6,8],[3,5,9],[4,8],[5,7,9,0],[6,8]];
    var keys = [observed.split('').map(v => parseInt(v))];
    keys[0].forEach((f,i) => { alts[f].forEach(a => {
      keys.forEach(k => { keys.push(k.slice(0,i).concat(a).concat(k.slice(i+1, k.length))); })
      })
    });
    return [...new Set(keys.map(m => m.join('')))];
  }

  //Previous Solution
  /*
  function getPINs(observed) {
  var keys = [observed.split('').map(v => parseInt(v))];
  for (var i = 0; i < keys[0].length; i++){
    getAlts(keys[0][i]).forEach(a => {
      for (var j = 0; j < keys.length; j++) if (keys[j][i] != a){
        keys.push(keys[j].slice(0, i).concat(a).concat(keys[j].slice(i+1, keys[j].length)));
      }
    });
  } 
  return [...new Set(keys.map(m => m.join('')))];
}

function getAlts(x){
  if (x == 0) return [0,8];
  
  var alts = [x];
  if (x % 3 != 0) alts.push(x+1);
  if ((x+2) % 3 != 0) alts.push(x-1);
  if (x > 3) alts.push(x - 3);
  if (x < 7) alts.push(x + 3);
  if (x == 8) alts.push(0);

  return alts;
}
  */