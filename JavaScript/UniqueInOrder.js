//https://www.codewars.com/kata/54e6533c92449cc251001667
var uniqueInOrder=function(u){
    if (!Array.isArray(u)) u = u.split('');
    for (var i = 1; i < u.length; i++) if (u[i-1] == u[i]) { u.splice(i,1); i--;}
    return u;
  }