import java.util.Scanner;

public class StringCompare {

    public static String getSmallestAndLargest(String s, int k) {
        String cur = s.substring(0, k);
        String smallest = cur;
        String largest = cur;

        for(int i = 1; i <= s.length()-k; i++)
        {
            cur = s.substring(i, i+k);

            if(cur.compareTo(smallest) < 0)
            {
                smallest = cur;
            }
            if(cur.compareTo(largest) > 0)
            {
                largest = cur;
            }
        }
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}