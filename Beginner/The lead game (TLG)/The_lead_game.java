/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class The_lead_game
{
	public static void main (String[] args) throws java.lang.Exception
	{
	   Scanner sc=new Scanner(System.in);
	   int n=sc.nextInt();
	   int a=0,b=0,max=0,l=0,m=0;
	   while(n-->0)
	   {
	       int x,y;
	        x=sc.nextInt();
	        l+=x;
	        y=sc.nextInt();
	        m+=y;
	       int diff=Math.abs(m-l);
	       if(diff>max)
	       {
	           max=diff;
	           a=x;
	           b=y;
	       }
	       
	   }
	   if(a>b)
	   {
	       System.out.println("1 "+max);
	   }
	   else
	   {
	       System.out.println("2 "+max); 
	   }
	}
}
