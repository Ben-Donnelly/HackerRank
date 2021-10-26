import java.util.*;
import java.util.stream.Collectors;


public class AnagramChecker {
    static boolean isAnagram(String a, String b) {
        Set<Character> charSetA = a.chars().mapToObj(chr -> (char) chr).collect(Collectors.toSet());

        for (char c : charSetA) {
           long stringACharCount =  a.chars().filter(ch -> ch == c).count();
           long stringBCharCount =  b.chars().filter(ch -> ch == c).count();

           if (stringACharCount != stringBCharCount) {
               return false;
           }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String a = scan.nextLine().toLowerCase();
        String b = scan.nextLine().toLowerCase();

        if (a.length() != b.length()) {
            System.out.println("Not Anagrams");
        } else {
            System.out.println(isAnagram(a, b) ? "Anagrams" : "Not Anagrams" );
        }
    }
}
