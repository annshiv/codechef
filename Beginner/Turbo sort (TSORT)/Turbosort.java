/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Turbosort
{
	public static void main (String[] args) throws java.lang.Exception
	{
	   Scanner sc=new Scanner(System.in);
	   int n=sc.nextInt();
	   int[] val=new int[n];
	   for(int i=0;i<n;i++)
	   {
	       val[i]=sc.nextInt();
	       
	   }
	   Arrays.sort(val);
	   for(int i:val)
	   {
	       System.out.println(i);
	   }
	}
}
