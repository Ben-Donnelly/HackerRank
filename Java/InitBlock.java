import java.util.*;

public class InitBlock {
    static Scanner scan = new Scanner(System.in);

    static int B = scan.nextInt();
    static int H = scan.nextInt();
    static boolean flag = true;

    static
    {
        try
        {
            if(B < 1 || H < 1)
            {
                flag = false;
                throw new Exception("Breadth and height must be positive");
            }
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }

    public static void main(String[] args){
        if(flag)
        {
            int area=B*H;
            System.out.print(area);
        }

    }//end of main

}//end of class

