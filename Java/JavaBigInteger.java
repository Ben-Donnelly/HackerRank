import java.math.BigInteger;
import java.util.Scanner;

public class JavaBigInteger {
    static BigInteger addBigInts(BigInteger a, BigInteger b) {
        return a.add(b);
    }

    static BigInteger multiplyBigInts(BigInteger a, BigInteger b) {
        return a.multiply(b);
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        BigInteger num1 = new BigInteger(scan.nextLine());
        BigInteger num2 = new BigInteger(scan.nextLine());

        System.out.println(addBigInts(num1, num2));
        System.out.println(multiplyBigInts(num1, num2));
    }
}
