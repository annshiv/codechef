import java.util.Scanner;

public class Main
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int s[]=new int[n];
        int m[]=new int[n];
        for(int i=0;i<n;i++)
        {
            s[i]=sc.nextInt();
            m[i]=sc.nextInt();
        }
        for(int i=0;i<n;i++)
        {
            System.out.printf("%d",(s[i]%m[i]));
            System.out.println();
        }
        
    }
}