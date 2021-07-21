//https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
using System;

public static class Kata 
{
  public static int TrailingZeros(int n)
  {
    int ret = 0;
    for (var i = 5; n/i >= 1; i *= 5) ret += (n/i) ;
    return ret;
  }
}