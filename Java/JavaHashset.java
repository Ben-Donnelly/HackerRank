import java.util.HashSet;
import java.util.Scanner;

public class JavaHashset {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int numOfPairs = Integer.parseInt(scan.nextLine());

        HashSet<String> pairsOfStrings = new HashSet<>();

        String [] stringSeparated;
        while (numOfPairs-- > 0) {
            stringSeparated = scan.nextLine().split("\\s");
            // You could just do <%s<insert non alpha char here>%s>
            // because the problem says its alpha chars only
            // But for ease of readability when debugging
            // I did it this way
            pairsOfStrings.add(String.format("{%s}{%s}", stringSeparated[0], stringSeparated[1]));
            System.out.println(pairsOfStrings.size());
        }
    }
}
