/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args)
	{
		Scanner sc=new Scanner(System.in);
	     int am=sc.nextInt();
		double bal=sc.nextDouble();
		if(am%5!=0 ||am+0.5>bal || bal==0.0)
		{
		    System.out.printf("%.2f",bal);
		}
		else
		    {
		        double r=bal-(double)am-0.5;
		        System.out.printf("%.2f",r);
		    }
	
	}
}
