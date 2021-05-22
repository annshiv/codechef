/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Sumofdigits
{
	public static void main (String[] args) 
	{
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int val[]=new int[n];
	
		for(int i=0;i<n;i++)
		{  
		  
		    val[i]=sc.nextInt();
		    
		  }
		  for(int i=0;i<n;i++)
		{  
		  
		   int sum=0;
		   for(int j=val[i];j>0;j/=10)
		   {
		    int r=j%10;
		   sum=sum+r;
		   
		   }
		   System.out.println(sum);
		   
		  }
	}
}
