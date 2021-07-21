//https://www.codewars.com/kata/520b9d2ad5c005041100000f
function pigIt(str){  
    var words = str.replace(/[^A-Z0-9a-z\s]/i,'').split(" ");
    for (var w = 0; w < words.length; w++){
      if (words[w].length > 0){    
        words[w] = words[w].slice(1,words[w].length) + words[w][0] + "ay";    
      }
      else {
        words.splice(w,1);
      }
    }
    if (str.search(/[^A-Z0-9a-z\s]/i) > 0) {
      words.push(str[str.length-1]);
    }
    return words.join(" ");
  }