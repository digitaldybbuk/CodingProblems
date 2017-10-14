using System;
using System.Diagnostics;
using System.Collections.Concurrent;
using System.Collections.Generic;
// Non-Empty Zero-Indexed Array A of N integers
// Each element is paired an even number of times, except for one element
// Goal: Return that element
// Example: A = [9,3,9,3,9,7,9] Return: 7
// Example: A = [9,3,9,3,9,2,9,2,2] Return: 2

class OddOccurrences : Solution
{
    static void Main()
    {
        Console.WriteLine("Odd Occurrences Problem");
        int[] Test = new int[] { 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1, 77, 77, 77};
        Console.WriteLine("Solution: " + solution(Test));
    }
}

class Solution
{
    public static int solution(int[] A)
    {
        ConcurrentDictionary<int, int> dict = new ConcurrentDictionary<int, int>();
        for (int i = 0; i < A.Length; i++)
        {
            dict.AddOrUpdate(A[i], 1, (key, count) => count + 1);
        }

        foreach (KeyValuePair<int, int> entry in dict)
        {
            if (entry.Value % 2 == 1)
            {
                return entry.Key;
            }
        }
        return 0;
    }
}