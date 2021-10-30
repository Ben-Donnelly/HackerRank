import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class TagContentExtractor {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Pattern validTagAndContent = Pattern.compile("<(.+)>([^<]+)</\\1>");
        Matcher validContentMatcher;
        boolean matchFound;

        int numberOfEntries = Integer.parseInt(scan.nextLine());

        while (numberOfEntries-- > 0){
            matchFound = false;
            String input = scan.nextLine();
            validContentMatcher = validTagAndContent.matcher(input);

            while (validContentMatcher.find()) {
                System.out.println(validContentMatcher.group(2));
                matchFound = true;
            }
            if(!matchFound) {
                System.out.println("None");
            }
        }
    }
}