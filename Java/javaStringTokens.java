import java.util.ArrayList;
import java.util.Arrays;
import java.util.*;
public class javaStringTokens {

    public static void tokenize(String input) {
        String deliminators = "[\s!,?._'@]";
        ArrayList<String> tokens = new ArrayList<>(Arrays.asList(input.split(deliminators)));
        tokens.removeIf(String::isBlank);

        int numOfTokens = tokens.size();
        if(numOfTokens < 1 || numOfTokens > 400000) {
            System.out.println(numOfTokens < 1 ? "String too small" : "String too large");
            return;
        }

        System.out.println(numOfTokens);
        for(String entry : tokens) {
            System.out.println(entry);
        }
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        scan.close();

        tokenize(input);
    }
}
