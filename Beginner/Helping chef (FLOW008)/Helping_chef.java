/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Helping_chef
{
	public static void main (String[] args) throws java.lang.Exception
	{
       Scanner sc=new Scanner(System.in);
       int n=sc.nextInt();
       for(int i=0;i<n;i++)
       {
           int num=sc.nextInt();
           if(num<10)
           {
               System.out.println("Thanks for helping Chef!");
           }
           else
           {
               System.out.println("-1");
           }
       }
	}
}
