import java.util.*;

public class IfElse {
    private static final Scanner scanner = new Scanner(System.in);

    public static void isNumWeird(int num)
    {
        String response = "Not Weird";

        if(num % 2 != 0 || num >= 6 && num <= 20)
        {
            response = "Weird";
        }

        System.out.println(response);
    }

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        scanner.close();

        isNumWeird(N);
    }
}
