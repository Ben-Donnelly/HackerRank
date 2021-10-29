import java.util.Scanner;
import java.util.regex.Pattern;
public class ValidUsernameChecker {
    public static void main(String[] args) {
        Pattern validUsername = Pattern.compile("[A-Za-z][\\w]{7,29}");
        Scanner scan = new Scanner(System.in);

        while(scan.hasNext()) {
            String username = scan.next();
            System.out.println(validUsername.matcher(username).matches() ? "Valid" : "Invalid");
        }
    }
}
