import java.util.*;

class loopsII{
    public static void sol(int a, int b, int n)
    {
        int calc = a;

        for(int i = 0; i < n; i++)
        {
            // calc += (int)(Math.pow(2, i) * b);
            calc += (1 << i) * b;
            System.out.print(calc + " ");
        }
        System.out.println();
    }
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++)
        {
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            sol(a, b, n);
        }
        in.close();
    }
}
