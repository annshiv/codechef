/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Valid_tri
{
	public static void main (String[] args) 
	{
		Scanner sc=new Scanner(System.in);
		int sum=0;
		int n1=sc.nextInt();
		for(int i=0;i<n1;i++)
		{
		    int val=sc.nextInt();
		    int val2=sc.nextInt();
		    int val3=sc.nextInt();
		    if((val3+val2+val)==180)
		{
		   System.out.println("YES");
		}
		else
		{
		    System.out.println("NO");
		}
		}
		
		
	}
}
