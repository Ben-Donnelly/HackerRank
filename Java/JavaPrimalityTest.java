import java.math.BigInteger;
import java.util.Scanner;

public class JavaPrimalityTest {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String binIntInput = scan.nextLine();
        scan.close();

        BigInteger numToTest = new BigInteger(binIntInput);
        System.out.println(numToTest.isProbablePrime(1) ? "prime" : "not prime");
    }
}
