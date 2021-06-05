/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Lucky_four
{
	public static void main (String[] args) throws java.lang.Exception
	{
      Scanner sc=new Scanner(System.in);
      int n=sc.nextInt();
      for(int i=0;i<n;i++)
      {
          int count=0;
          int val=sc.nextInt();
          while(val>0)
          {
              int r=val%10;
              if(r==4)
              {
                  count++;
              }
              val=val/10;
              
          }
          System.out.println(count);
      }
	}
}
