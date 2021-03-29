import java.util.*;

public class Palindrome {

    public static String isPal(String s1)
    {

        // StringBuilder rev = new StringBuilder(a).reverse();
        // System.out.println(a.equals(rev.toString()) ? "Yes" : "No" );

        char p1, p2;

        while(s1.length() > 1)
        {
            p1 = s1.charAt(0);
            p2 = s1.charAt(s1.length()-1);

            if(!(p1 == p2))
            {
                return "No";
            }

            s1 = s1.substring(1, s1.length()-1);
        }
        return "Yes";
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        sc.close();

        System.out.println(isPal(a));
    }
}



