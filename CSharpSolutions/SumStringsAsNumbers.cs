//https://www.codewars.com/kata/5324945e2ece5e1f32000370
using System;
using System.Collections.Generic;
public static class Kata
{
    public static string sumStrings(string a, string b)
    {
      var ret = new List<char>();
      int maxLength = (a.Length > b.Length)? a.Length : b.Length;
      int remainder = 0;
      for (int i = 1; i <= maxLength ; i++)
      {
         int x = 0; int y = 0;
         if (i <= a.Length) { int.TryParse(a[a.Length-i].ToString(), out x); }
         if (i <= b.Length) { int.TryParse(b[b.Length-i].ToString(), out y); }
         
         int r = (x+y+remainder);
         ret.Add((r%10).ToString()[0]);
         remainder = (r - (r%10))/10;
      }
      if (remainder > 0) { ret.Add(remainder.ToString()[0]); }
      ret.Reverse();
      while (ret[0] == '0'){ ret.RemoveAt(0);}
      return new string(ret.ToArray());
    }
}