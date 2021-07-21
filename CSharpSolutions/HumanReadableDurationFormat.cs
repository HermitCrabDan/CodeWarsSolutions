//https://www.codewars.com/kata/52742f58faf5485cae000b9a
public class HumanTimeFormat{
  public static string formatDuration(int seconds){
    //Enter Code here
    if (seconds == 0) return "now";
    
    var ret = "";
    int t = 0;
    
    int y = seconds/(60 * 60 * 24 * 365);  
    if (y > 0) 
    { 
      ret = ret + y + " year"; 
      if (y > 1) ret = ret+"s";
      t++; 
      seconds %= (60 * 60 * 24 * 365); 
    }
    
    int d = seconds / (60 * 60 * 24);
    if (d > 0) 
    { 
      ret = (t>0)? ret +  ", " + d + " day" : ret + d + " day"; 
      if (d > 1) ret = ret+"s";
      t++; 
      seconds %= (60 * 60 * 24); 
    }
    
    int h = seconds / (60 * 60); 
    if (h > 0) 
    { 
      ret = (t>0)? ret + ", " + h + " hour": ret + h + " hour"; 
      if (h > 1) ret = ret+"s";
      t++; 
      seconds %= (60 * 60); 
    }
    
    int m = seconds / 60;
    if (m > 0) 
    { 
      ret = (t>0)? ret + ", " + m + " minute": ret + m + " minute"; 
      if (m > 1) ret = ret+"s";
      t++; 
      seconds %= 60; 
    }
    
    if (seconds > 0) 
    { 
      ret = (t>0)? ret + ", " + seconds + " second": ret + seconds + " second"; 
      if (seconds > 1) ret = ret+"s";
    }
    
    t = ret.LastIndexOf(",");
    if (t > 0) ret = ret.Substring(0,t) + " and" + ret.Substring(t+1); 
        
    return ret;
  }
}