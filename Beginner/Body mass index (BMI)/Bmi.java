import java.util.*;

class Bmi 
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int w=sc.nextInt();
        int h=sc.nextInt();
        int m=w/(h*2);
        if(m<18)
        {
            System.out.println("Week body");
        }
        else if(m>=18 && m<=26)
        {
            System.out.println("normal body");
        }
        else
        {
            System.out.println("fat body");
        }
    }
}