//https://www.codewars.com/kata/523a86aa4230ebb5420001e1
function anagrams(word, words) {
    sorted = word.split('').sort().join('');
    return words.filter(function(w) { return w.split('').sort().join('') == sorted });
  }

//Previous Solution
/*
function anagrams(word, words) {
  var ans = [];
  var letters = word.split('').concat().sort();
  for (w = 0; w < words.length; w++){
    wl = words[w].split('').concat().sort();
    if (wl.length == letters.length){
      var add = true;
      for (i = 0; i < letters.length; i++){
        if (wl[i] != letters[i]){
          add = false;
        }
      }
      if (add == true) { ans.push(words[w]); }
    }
  }
  return ans;
}
*/