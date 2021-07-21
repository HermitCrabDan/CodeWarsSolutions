//https://www.codewars.com/kata/546f922b54af40e1e90001da
function alphabetPosition(text) {
    return text.replace(/\W/g, '')
      .toUpperCase()
      .split('')
      .map(function(item){ var cd = item.charCodeAt(0); if (cd > 64 && cd < 91) { return cd - 64; }})
      .filter(Boolean)
      .join(' ');
  }