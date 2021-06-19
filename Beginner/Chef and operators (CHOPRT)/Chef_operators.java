/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Chef_operators
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    Scanner sc=new Scanner(System.in);
	    int n=sc.nextInt();
	    for(int i=0;i<n;i++)
	    {
	    int num1=sc.nextInt();
	    int num2=sc.nextInt();
	    
	    
	    if(num1>num2)
	    {
	        System.out.println(">");
	    }
	    else if(num1<num2)
	    {
	        System.out.println("<");
	    }
	    else
	    {
	        System.out.println("=");
	    }
	    }
 	}
}
