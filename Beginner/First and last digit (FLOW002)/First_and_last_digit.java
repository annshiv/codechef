/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class First_and_last_digit
{
	public static void main (String[] args) 
	{
		 Scanner sc=new Scanner(System.in);
		 int n=sc.nextInt();
		for(int i=0;i<n;i++)
		{
		    int num=sc.nextInt();
		    String str=String.valueOf(num);
		    char l=str.charAt(str.length()-1);
		    char f=str.charAt(0);
		    System.out.println(Character.getNumericValue(f)+Character.getNumericValue(l));
		    
		}
	}
}
