/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Second_lar
{
	public static void main (String[] args) throws java.lang.Exception
	{
	   Scanner sc=new Scanner(System.in);
	   int n=sc.nextInt();
	   int a=0,b=0,c=0;
	   for(int i=0;i<n;i++)
	   {
	       a=sc.nextInt();
	       b=sc.nextInt();
	       c=sc.nextInt();
	       
	   
	   try {
	       if((a>b && c>a)||(a>c && a<b))
	       {
	           System.out.println(a);
	       }
	       else if((b>a && c>b) || (b>c && b<a))
	       {
	           System.out.println(b);
	           
	       }
	       else
	       {
	           System.out.println(c);
	       }
	       
	   } catch(Exception e) {
	       return ;
	   } 
	   }
	}
}
