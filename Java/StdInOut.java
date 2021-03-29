import java.util.Scanner;

public class StdInOut {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int i = scan.nextInt();
        double d = scan.nextDouble();

        scan.nextLine();
        String s1 = scan.nextLine();
        scan.close();

        System.out.printf("String: %s\nDouble: " + d + "\nInt: %d", s1, i);
    }
}
