//https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
public class Parser
{  
    public static int ParseInt(string s)
    {
        Dictionary<string, int> singleValues = new Dictionary<string, int>()
        {
            { "one", 1 }, { "two", 2}, { "three", 3 }, { "four", 4}, { "five", 5 },
            { "six", 6 }, { "seven", 7 }, { "eight", 8 }, { "nine", 9 },
            { "ten", 10 }, { "eleven", 11 }, { "twelve", 12 }, { "thirteen", 13 },
            { "fourteen", 14 }, { "fifteen", 15}, { "sixteen", 16 }, { "seventeen", 17 },
            { "eighteen", 18 }, { "nineteen", 19 },
            { "twenty", 20 }, { "thirty", 30 }, { "forty", 40 }, { "fifty", 50 },
            { "sixty", 60 }, { "seventy", 70 }, { "eighty", 80 }, { "ninety", 90 }
        };
        Dictionary<string, int> multiplierValues = new Dictionary<string, int>()
        {
            { "million", 1000000 }, { "thousand", 1000 }, { "hundred", 100 }
        };
        Console.WriteLine(s);
        s = s.ToLower();
        int result = 0;
        if (s != "zero")
        {                
            var wordList = s.Split(new string[] { " ", "-" } , StringSplitOptions.RemoveEmptyEntries);
            for (int i = 0; i < wordList.Length; i++)
            {
                bool singleValue = true;
                for (int k = 0; k < multiplierValues.Count; k++)
                {
                    for (int j = i; j < wordList.Length; j++)
                    {
                        if (wordList[j] == multiplierValues.ElementAt(k).Key)
                        {
                            singleValue = false;
                            int magnitude = multiplierValues[wordList[j]];
                            int multiplier = 0;
                            for (int l = i; l < j; l++)
                            {
                                if (singleValues.ContainsKey(wordList[l]))
                                {
                                    multiplier += singleValues[wordList[l]];
                                }
                                if (multiplierValues.ContainsKey(wordList[l]))
                                {
                                    multiplier *= multiplierValues[wordList[l]];
                                }
                            }
                            if (multiplier == 0) multiplier = 1;
                            result += multiplier * magnitude;

                            i = j;
                            break;
                        }
                    }
                }
                if (singleValue && singleValues.ContainsKey(wordList[i]))
                {
                    result += singleValues[wordList[i]];
                }
            }
                
        }
        return result;
    }
}