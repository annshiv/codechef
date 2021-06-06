/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Reverse_numbe
{
	public static void main (String[] args) throws java.lang.Exception
	{
		try 
		{
		    Scanner sc=new Scanner(System.in);
		    int n=sc.nextInt();
		    int rem=0;
		    for(int i=0;i<n;i++)
		    {
		    int num=sc.nextInt();
		    int sum=0;
		    while(num!=0)
		    {
		       rem=num%10;
		       sum=sum*10+rem;
		       num/=10;
		    }
		    System.out.println(sum);
		    }
		}catch(Exception e)
		{
		return;
		}
	}
}
