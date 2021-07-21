//https://www.codewars.com/kata/51fda2d95d6efda45e00004e
using System;
// TODO: create the User class/object
// it must support rank, progress, and the incProgress(int rank) method
public class User
{
  public User() { this.userRank = -8; }
  
  private int userRank;
  private int userProgress;
  
  public int rank
  {
    get{ return userRank; }
  }
  
  public int progress 
  { 
    get 
    { 
      if (userRank == 8) return 0;
      
      return userProgress; 
    } 
  }
  
  public void incProgress(int score)
  {
    if (score >= -8 && score <= 8 && score != 0)
    {
      if (score == userRank) userProgress += 3;
      else if (score == -1 && userRank == 1 || score == (userRank - 1)) userProgress++;
      else if (score > userRank)
      {
        var d = (score - userRank);
        if (score > 0 && userRank <0) d--;
        
        userProgress += 10 * d * d;
      }
      
      while (userProgress >= 100) 
      { 
        userRank++; 
        
        if (userRank == 0) userRank++; 
        if (userRank > 8) userRank = 8; 
        
        userProgress -= 100;
      }
      
    }
    else 
    {
      throw new ArgumentException();
    }
  }
  
}