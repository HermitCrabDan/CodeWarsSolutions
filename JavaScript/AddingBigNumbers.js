//https://www.codewars.com/kata/525f4206b73515bffb000b21
function add(a, b) {
    var ad = a.split('');
    var bd = b.split('');
    var max = (ad.length > bd.length)? ad.length: bd.length;
    var ret = [];
    var r = 0;
    for (var i = 1; i<= max; i++){
      var x = 0; var y = 0;
      if (i <= ad.length) x = Number(ad[ad.length - i]);
      if (i <= bd.length) y = Number(bd[bd.length - i]);
      var ans = x+y+r;
      ret.push((ans%10).toString());
      r = (ans - (ans%10))/10;
    }
    ret.push(r.toString());
    ret = ret.reverse();
    while (ret[0] == "0") ret.splice(0,1);
    return ret.join("");
  }