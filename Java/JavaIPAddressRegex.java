import java.util.regex.Pattern;
import java.util.Scanner;

class MyRegex {
    public boolean regexChecker(String ipAddress) {
        Pattern ipValidatorPattern = Pattern.compile("^(([0-1]?([0-9]){1,2}|2[0-4][0-9]|25[0-5])\\.){3}([0-1]?([0-9]){1,2}|2[0-4][0-9]|25[0-5])$");
        return ipValidatorPattern.matcher(ipAddress).matches();
    }
}

public class JavaIPAddressRegex {
    public static void main(String[] args) {
        MyRegex ipAddressCheck = new MyRegex();
        Scanner scan = new Scanner(System.in);

        while(scan.hasNext()) {
            String ip = scan.next();
            System.out.println(ipAddressCheck.regexChecker(ip));
        }
        scan.close();
    }
}

