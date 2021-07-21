//https://www.codewars.com/kata/51e056fe544cf36c410000fb
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
public class TopWords
{
    public static List<string> Top3(string s)
    {
        string[] sp = new string[] {" ",".","!","/","\n",",","_","-",":","?","<",">",";"};
        return s.ToLower()
          .Split(sp, StringSplitOptions.None)
          .Where(w => Regex.IsMatch(w, @"\w+[']{0,}[a-z]{0,}")) //"[a-zA-Z]{1,}[']{0,}[a-zA-z]{0,}"))
          .GroupBy(g => g)
          .OrderByDescending(o => o.Count())
          .Take(3)
          .Select(n => n.Key)
          .ToList();
        //return null;
    }
}