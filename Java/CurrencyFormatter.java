import java.util.Scanner;
import java.text.NumberFormat;
import java.util.Locale;

public class CurrencyFormatter {
    public static String formatNumber(Locale currentLocal, double payment) {
        return String.format("%s", NumberFormat.getCurrencyInstance(currentLocal).format(payment));
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        double payment = scan.nextDouble();
        scan.close();

        String us = formatNumber(Locale.US, payment);
        String india = formatNumber(new Locale("en", "IN"), payment);
        String china = formatNumber(Locale.CHINA, payment);
        String france =formatNumber(Locale.FRANCE, payment);


        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
