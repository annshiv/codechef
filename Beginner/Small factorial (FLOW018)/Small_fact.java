package Beginner.Small factorial (FLOW018);

/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class small_fact
{
	public static void main (String[] args) throws java.lang.Exception
	{
	   Scanner sc=new Scanner(System.in);
	   int n=sc.nextInt();
	   for(int i=0;i<n;i++)
	   {
	       int num=sc.nextInt();
	       System.out.println(factorial(num));
	   }
	   
	}
	static int factorial(int n)
	{
	    if(n==0)
	    {
	        return 1;
	    }
	    else
	    {
	        return (n*factorial(n-1));
	    }
	}
}

