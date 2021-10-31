import java.math.BigDecimal;
import java.util.*;

public class JavaBigDecimal {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int numOfEntries = scan.nextInt();
        BigDecimal [] entries = new BigDecimal[numOfEntries];

        for (int i=0; i<numOfEntries; i++) {
            entries[i] = new BigDecimal(scan.next());
        }
        scan.close();

        Comparator<BigDecimal> customComparator = BigDecimal::compareTo;
        Arrays.sort(entries, 0, numOfEntries, customComparator);

        for(BigDecimal i : entries) {
            System.out.println(i);
        }
    }
}
