import java.util.Scanner;
import java.util.regex.*;

public class PatternSyntaxChecker
{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        int testCases = Integer.parseInt(in.nextLine());
        String re;

        while(testCases > 0)
        {
            re = in.nextLine();
            try
            {
                Pattern.compile(re);
                System.out.println("Valid");
            }
            catch(Exception e)
            {
                System.out.println("Invalid");
            }
            testCases--;
        }
    }
}



