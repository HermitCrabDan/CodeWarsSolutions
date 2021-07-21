//https://www.codewars.com/kata/51b66044bce5799a7f000003
var RomanNumerals = function(){
    return {
      toRoman: function(x){
         var ret = [];
         
         while (x >= 1000) { ret.push('M'); x-= 1000; }
         if (x >= 900) { ret.push('CM'); x -= 900; }
         if (x >= 500) { ret.push('D'); x-= 500; }
         while (x >= 100) { ret.push('C'); x -= 100; }
         if (x >= 90) { ret.push('XC'); x-=90; }
         if (x >=50) { ret.push('L'); x -= 50; };
         while (x >= 10) { ret.push('X'); x-= 10; }
         if (x == 9) { ret.push('IX'); x -= 9; }
         if (x >= 5) { ret.push('V'); x -= 5; }
         if (x == 4) { ret.push('IV'); x -= 4; }
         while (x > 0) {ret.push('I'); x--; }
         
         return ret.join('');
       }
       ,fromRoman: function(r){
         var v = 0;
         
         while(r.search("CM") != -1){ v += 900; r = r.replace("CM",""); }
         while(r.search("M") != -1){ v += 1000; r = r.replace("M",""); }
         while(r.search("D") != -1){ v += 500; r = r.replace("D",""); }
         while(r.search("XC") != -1){ v += 90; r = r.replace("XC",""); }
         while(r.search("C") != -1){ v += 100; r = r.replace("C",""); }
         while(r.search("L") != -1){ v += 50; r = r.replace("L",""); }
         while(r.search("IX") != -1){ v += 9; r = r.replace("IX",""); }
         while(r.search("X") != -1){ v += 10; r = r.replace("X",""); }
         while(r.search("IV") != -1){ v += 4; r = r.replace("IV",""); }
         while(r.search("V") != -1){ v += 5; r = r.replace("V",""); }
         while(r.search("I") != -1){ v += 1; r = r.replace("I",""); }
         
         return v;
       }
      }
    }();