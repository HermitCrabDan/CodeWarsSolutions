//https://www.codewars.com/kata/5262119038c0985a5b00029f
public static class Kata
{
  public static bool IsPrime(int n)
  {
    if (n > 2 && n % 2 == 0) return false;
    for (var m = 3; m*m <= n; m += 2) if (n % m == 0) return false;
    return (n >= 2);
  }
}

//Previous solution
/*
public static class Kata
{
  public static bool IsPrime(int n)
  {
    if (n > 2 && n % 2 == 0) return false;
    for (var m = 3; m*m <= n; m = m+2)
    {
      if (n % m == 0) return false;
    }
    return (n >= 2);
  }
}
*/