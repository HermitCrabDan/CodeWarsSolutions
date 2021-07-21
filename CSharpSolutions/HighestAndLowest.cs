//https://www.codewars.com/kata/554b4ac871d6813a03000035
using System;

public static class Kata
{
  public static string HighAndLow(string numbers)
  {
    // Code here or
    if (!String.IsNullOrEmpty(numbers))
    {
      string [] numstrings = numbers.Split(' ');
      int? max = null;
      int? min = null;
      
      for (int i = 0; i < numstrings.Length; i++)
      {
        int output = 0;
        if (int.TryParse(numstrings[i], out output))
        {
          if (!max.HasValue || output > max.Value)
          {
            max = output;
          }
          if (!min.HasValue || output < min.Value)
          {
            min = output;
          }
        }
      }
      return String.Format("{0} {1}"
        , max
        , min
        );
    }
    else
      return "";
  }
}