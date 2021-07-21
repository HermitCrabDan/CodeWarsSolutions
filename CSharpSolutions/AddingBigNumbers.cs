//https://www.codewars.com/kata/525f4206b73515bffb000b21
using System;

public class Kata
{
  public static string Add(string a, string b)
  {
    int r = 0;
    int l = (a.Length > b.Length)? a.Length:b.Length;
    var ret = new System.Collections.Generic.Stack<char>();
    for (int i = 1; i <= l; i++)
    {
      int x = 0; int y = 0;
      if (i <= a.Length) int.TryParse(a[a.Length - i].ToString(), out x);
      if (i <= b.Length) int.TryParse(b[b.Length - i].ToString(), out y);
      ret.Push(((x+y+r)%10).ToString()[0]);
      r = ((x+y+r) - ((x+y+r)%10))/10;
    }
    ret.Push(r.ToString()[0]);
    while (ret.Peek() == '0') ret.Pop();
    return new string(ret.ToArray());
  }
}
//Previous Solution
/*
using System;
using System.Collections.Generic;

public class Kata
{
  public static string Add(string a, string b)
  {
    var ret = new List<char>();
    var max = (a.Length > b.Length)? a.Length : b.Length;
    var r = 0;
    for (int i = 1; i <= max; i++)
    {
      int x = 0; int y = 0;
      if (i <= a.Length) { int.TryParse(a[a.Length - i].ToString(), out x); }
      if (i <= b.Length) { int.TryParse(b[b.Length - i].ToString(), out y); }
      
      int ans = x+y+r;
      ret.Add((ans % 10).ToString()[0]);
      r = (ans - (ans % 10))/10;
    }
    
    ret.Add(r.ToString()[0]);
    ret.Reverse();
    
    while (ret.Count > 0 && ret[0] == '0') ret.RemoveAt(0);
    
    return new string(ret.ToArray());
  
  }
}
*/