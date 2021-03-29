import java.util.*;
public class Strings {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();

        int tot_length;
        String isLexBigger;
        String finalString;

        tot_length = a.length() + b.length();
        isLexBigger = a.compareTo(b) > 0 ? "Yes":"No"; // ♪Maybe♪

        finalString = Character.toUpperCase(a.charAt(0)) + a.substring(1) + " " + Character.toUpperCase(b.charAt(0)) + b.substring(1);

        System.out.printf("%d%n%s%n%s", tot_length, isLexBigger, finalString);
    }
}



