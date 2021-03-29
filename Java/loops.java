import java.util.*;

public class loops {
    private static final Scanner scanner = new Scanner(System.in);

    static void calculation(int num)
    {
        for(int i = 1; i < 11; i++)
        {
            int calc = num * i;
            System.out.printf("%d x %d = %d%n", num, i, calc);
        }
    }

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        scanner.close();

        calculation(N);
    }
}
