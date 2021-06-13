/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Find_square_root 
    
{
	public static void main (String[] args) throws java.lang.Exception
	{
	   Scanner sc=new Scanner(System.in);
	   int n=sc.nextInt();
	   while(n-->0)
	   {
	       int num=sc.nextInt();
	       double val=Math.sqrt(num);
	       int number=(int)Math.floor(val);
	       System.out.println(number);
	   }
	}
}
